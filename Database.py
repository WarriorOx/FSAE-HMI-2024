import sqlite3

connection = sqlite3.connect("fsae.db")

cursor = connection.cursor()
#cursor.execute("CREATE TABLE fsae_database (Date TEXT, Time TEXT, Parameter TEXT, Value INTEGER )")

table_schema = '''
    CREATE TABLE IF NOT EXISTS telemetry_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Speed REAL,
        MotorTemperature REAL,
        CoolantTemperature REAL,
        CoolantFlowRate REAL,
        MotorCurrent REAL,
        BatteryVoltage REAL,
        BatteryTemperature REAL,
        LVBatteryVoltage REAL,
        GPSLocation TEXT,
        Acceleration3Axis TEXT,
        Direction3Axis TEXT,
        LapTime REAL
    );
'''
cursor.execute(table_schema)


