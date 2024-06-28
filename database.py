import psycopg2
from dotenv import load_dotenv
import os

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
    cursor.execute(f"SELECT * FROM translators WHERE translators.name = '{translator}'")
    response = cursor.fetchall()[-1]
    print(response)
    # cursor.execute(f'SELECT (girl_name, month_balance, day_balance) FROM data WHERE translator == {translator}')
    return [{'name': response[0], 'girl_name': response[1], 'month_balance': response[2], 'day_balance': response[3]}]
    # if len(cursor.fetchall()) == 1:
    # return [cursor.fetchall()[-1], {'girl_name': None, 'month_balance': None, 'day_balance': None}]
    # return cursor.fetchall()


def delete_translator(translator_id: int) -> bool | int:
    cursor.execute(f"DELETE FROM translators WHERE translators.name = '{translator_id}'")
    database.commit()
    cursor.execute(f"SELECT name FROM translators WHERE translators.name = '{translator_id}'")
    if cursor.fetchall():
        return False
    else:
        return translator_id


def get_translators(admin_id: int) -> list:
    cursor.execute(f"SELECT name FROM translators WHERE translators.admin_name = '{admin_id}'")
    response = cursor.fetchall()
    return [val[0] for val in response]


def register_translator(translator_id: int, admin_id: int):
    try:
        cursor.execute(f"INSERT INTO translators(name, time, girl1_name, girl2_name, admin_name)"
                       f"SELECT '{translator_id}', 0, 'None', 'None', '{admin_id}' "
                       f"WHERE "
                       f"NOT EXISTS ("
                       f"SELECT name FROM translators WHERE name = '{translator_id}'"
                       f");")
        database.commit()
        return True
    except Exception as e:
        return e


def get_admins() -> list:
    try:
        cursor.execute(f"SELECT name FROM admins")
        response = cursor.fetchall()
        return [val[0] for val in response]
    except Exception as e:
        print(e)
        return []


def get_keys() -> list:
    try:
        cursor.execute(f'SELECT key FROM keys')
        return cursor.fetchall()
    except Exception as e:
        print(e)
        return []
