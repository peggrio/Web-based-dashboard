from flask import Flask, jsonify, render_template
from dotenv import dotenv_values
import psycopg2
import os

app = Flask(__name__)

env_vars = dotenv_values('local.env')

table_name_1 = "CM_HAM_DO_AI1/Temp_value"
table_name_2 = "CM_HAM_PH_AI1/pH_value"
table_name_3 = "CM_PID_DO/Process_DO"
table_name_4 = "CM_PRESSURE/Output"

@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8888'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response

@app.route('/')
def home():
    os.system("python3 ./config.py") #this only need to be executed one time
    try:
        # Connect to the database
        conn = psycopg2.connect(database=env_vars['POSTGRES_DB'],
                                user=env_vars['POSTGRES_USER'],
                                password=env_vars['POSTGRES_PASSWORD'],
                                host=env_vars['POSTGRES_HOST'],
                                port=env_vars['POSTGRES_PORT'])
        cur = conn.cursor()

        # SQL query to retrieve data from the table
        select_sql = f"SELECT time, temperature FROM public. \"{table_name_1}\" ORDER BY time"

        # Execute the SQL query
        cur.execute(select_sql)

        # Fetch all the rows returned by the query
        rows = cur.fetchall()
        time = [row[0] for row in rows]
        temperature = [row[1] for row in rows]
        data_temp = ({"time":time,"value":temperature})

        # print(data_temp)

        select_sql = f"SELECT time, pH FROM public. \"{table_name_2}\" ORDER BY time"
        cur.execute(select_sql)
        rows = cur.fetchall()
        time = [row[0] for row in rows]
        pH = [row[1] for row in rows]
        data_ph = ({"time":time,"value":pH})

        print(data_ph)

        select_sql = f"SELECT time, Distilled_Oxygen FROM public. \"{table_name_3}\" ORDER BY time"
        cur.execute(select_sql)
        rows = cur.fetchall()
        time = [row[0] for row in rows]
        Distilled_Oxygen = [row[1] for row in rows]
        data_do = ({"time":time,"value":Distilled_Oxygen})

        # print(data_do)

        select_sql = f"SELECT time, Pressure FROM public. \"{table_name_4}\" ORDER BY time"
        cur.execute(select_sql)
        rows = cur.fetchall()

        time = [row[0] for row in rows]
        Pressure = [row[1] for row in rows]
        data_Pressure = ({"time":time,"value":Pressure})
        # print(data_Pressure)

        # Close the cursor and connection
        cur.close()
        conn.close()

        data=[data_temp, data_ph, data_do, data_Pressure]
        # print(data)
        return data

    except Exception as e:
        print(e)
        return {"error": str(e)}


if __name__ == "__main__":
    app.run(port=5001,debug=True)
