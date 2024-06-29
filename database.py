import os
import psycopg2
from dotenv import load_dotenv

load_dotenv('settings.env')
HOST = os.getenv('DATABASE_HOST')
USER = os.getenv('DATABASE_USER')
PASS = os.getenv('DATABASE_PASS')


database = psycopg2.connect(
  host=HOST,
  user=USER,
  password=PASS
)
cursor = database.cursor()


def get_translator_data(translator) -> list[dict]:
    cursor.execute(f"SELECT girls.name, daily_balance, month_balance "
                   f"FROM translators "
                   f"INNER JOIN girls ON girls.name = translators.girl1_name OR girls.name = translators.girl2_name "
                   f"WHERE translators.name = '{translator}'")
    response = cursor.fetchall()
    answer = []
    for data in response:
        answer.append({'girl_name': data[0], 'day_balance': data[1], 'month_balance': data[2]})
    return answer


def delete_translator(translator_id: int) -> bool | int:
    cursor.execute(f"DELETE FROM translators "
                   f"WHERE translators.name = '{translator_id}'"
                   f"RETURNING name;")
    database.commit()
    if cursor.fetchall():
        return False
    else:
        return translator_id


def get_translators(admin_id: int) -> list:
    cursor.execute(f"SELECT name FROM translators WHERE translators.admin_name = '{admin_id}'")
    response = cursor.fetchall()
    return [val[0] for val in response]


def register_translator(translator_id: int, admin_id: int) -> bool | Exception:
    try:
        cursor.execute(f"SELECT name FROM translators WHERE translators.name = '{translator_id}'")
        if cursor.fetchone():
            return False
        else:
            cursor.execute(f"INSERT INTO translators(name, time, girl1_name, girl2_name, admin_name)"
                           f"SELECT '{translator_id}', 0, 'None', 'None', '{admin_id}' "
                           f"WHERE "
                           f"NOT EXISTS ("
                           f"SELECT name FROM translators WHERE name = '{translator_id}')")
            database.commit()
            return True
    except Exception as e:
        raise e


def get_admins() -> list:
    try:
        cursor.execute(f"SELECT name FROM admins")
        response = cursor.fetchall()
        return [val[0] for val in response]
    except Exception as e:
        print(e)
        return []


def get_admin(translator_id: int) -> int | None:
    try:
        cursor.execute(f"SELECT admin_name FROM translators WHERE admin_name = '{translator_id}'")
        response = cursor.fetchone()
        return response[-1]
    except Exception as e:
        print(e)
        return None


def get_keys() -> list:
    try:
        cursor.execute(f'SELECT key FROM keys')
        return cursor.fetchall()
    except Exception as e:
        print(e)
        return []
