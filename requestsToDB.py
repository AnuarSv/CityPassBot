import psycopg2
from config import host, user, password, port, db_name


async def db() -> list[str]:
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            port=port,
            password=password,
            database=db_name
        )
        cursor = connection.cursor()
        cursor.execute("""
            SELECT landmark_name
            FROM landmarks;
        """)
        column_names = [row[0] for row in cursor.fetchall()]
        return column_names
    except Exception as _ex:
        return f"An error occurred. {_ex}"
    finally:
        if connection:
            cursor.close()
            connection.close()


async def db_choose(name) -> str:
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            port=port,
            password=password,
            database=db_name
        )
        cursor = connection.cursor()
        cursor.execute(f"""
            SELECT landmark_name, landmark_description, landmark_location
            FROM landmarks WHERE landmark_name = '{name}';
        """)
        result = cursor.fetchone()
        if result:
            output = f"{result[0]}\n{result[1]}\n{result[2]}"
            return output
        else:
            return "Landmark not found."
    except Exception as _ex:
        return f"An error occurred. {_ex}"
    finally:
        if connection:
            cursor.close()
            connection.close()

