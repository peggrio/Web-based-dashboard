import psycopg2
from dotenv import dotenv_values
from psycopg2.extras import execute_values

# Load the environment variables from the local.env file
env_vars = dotenv_values('local.env')

conn = psycopg2.connect(database=env_vars['POSTGRES_DB'],
                        user=env_vars['POSTGRES_USER'],
                        password=env_vars['POSTGRES_PASSWORD'],
                        host=env_vars['POSTGRES_HOST'],
                        port=env_vars['POSTGRES_PORT'])

cur = conn.cursor()

table_name_1 = "CM_HAM_DO_AI1/Temp_value"
table_name_2 = "CM_HAM_PH_AI1/pH_value"
table_name_3 = "CM_PID_DO/Process_DO"
table_name_4 = "CM_PRESSURE/Output"

query_1 = f"CREATE TABLE IF NOT EXISTS public. \"{table_name_1}\"(time TIMESTAMP WITHOUT TIME ZONE,temperature DOUBLE PRECISION);COMMENT ON TABLE public. \"{table_name_1}\" IS 'Table to store Temperature data in Celsius'"
query_2 = f"CREATE TABLE IF NOT EXISTS public. \"{table_name_2}\"(time TIMESTAMP WITHOUT TIME ZONE,pH DOUBLE PRECISION);COMMENT ON TABLE public. \"{table_name_2}\" IS 'Table to store pH data'"
query_3 = f"CREATE TABLE IF NOT EXISTS public. \"{table_name_3}\"(time TIMESTAMP WITHOUT TIME ZONE,Distilled_Oxygen DOUBLE PRECISION);COMMENT ON TABLE public. \"{table_name_3}\" IS 'Table to store Distilled Oxygen data in %'"
query_4 = f"CREATE TABLE IF NOT EXISTS public. \"{table_name_4}\"(time TIMESTAMP WITHOUT TIME ZONE,Pressure DOUBLE PRECISION);COMMENT ON TABLE public. \"{table_name_4}\" IS 'Table to store Pressure data in psi'"

cur.execute(query_1)
cur.execute(query_2)
cur.execute(query_3)
cur.execute(query_4)

# List of rows to be inserted
temp_data = [
    ('2023-04-30 12:00:00', 30.0),
    ('2023-04-30 12:01:00', 26.0),
    ('2023-04-30 12:02:00', 27.0),
    ('2023-04-30 12:03:00', 28.0),
]

pH_data = [
    ('2023-04-30 12:00:00', 7.2),
    ('2023-04-30 12:01:00', 7.4),
    ('2023-04-30 12:02:00', 7.0),
    ('2023-04-30 12:03:00', 7.1)
]

do_data = [
    ('2023-04-30 12:00:00', 60.5),
    ('2023-04-30 12:01:00', 61.0),
    ('2023-04-30 12:02:00', 62.2),
    ('2023-04-30 12:03:00', 63.1)
]

pressure_data = [
    ('2023-04-30 12:00:00', 10.2),
    ('2023-04-30 12:01:00', 10.1),
    ('2023-04-30 12:02:00', 10.0),
    ('2023-04-30 12:03:00', 9.9)
]
# SQL statement to insert multiple rows
insert_sql_1 = f"INSERT INTO public. \"{table_name_1}\" (time, temperature) VALUES %s"
insert_sql_2 = f"INSERT INTO public. \"{table_name_2}\" (time, pH) VALUES %s"
insert_sql_3 = f"INSERT INTO public. \"{table_name_3}\" (time, Distilled_Oxygen) VALUES %s"
insert_sql_4 = f"INSERT INTO public. \"{table_name_4}\" (time, Pressure) VALUES %s"

update_sql_1 = f"UPDATE public. \"{table_name_1}\" SET temperature = %s WHERE time = %s"
update_sql_2 = f"UPDATE public. \"{table_name_2}\" SET pH = %s WHERE time = %s"
update_sql_3 = f"UPDATE public. \"{table_name_3}\" SET Distilled_Oxygen = %s WHERE time = %s"
update_sql_4 = f"UPDATE public. \"{table_name_4}\" SET Pressure = %s WHERE time = %s"

# Execute the SQL statement to insert the rows
execute_values(cur, insert_sql_1, temp_data)
execute_values(cur, insert_sql_2, pH_data)
execute_values(cur, insert_sql_3, do_data)
execute_values(cur, insert_sql_4, pressure_data)

conn.commit()

cur.close()

conn.close()
