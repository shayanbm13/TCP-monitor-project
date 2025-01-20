import sqlite3

class SmartHomeDatabase:
    def __init__(self, db_name='database.db'):
        self.db_name = db_name

    def create_database(self):
        # ایجاد یک اتصال به دیتابیس یا اتصال به دیتابیس موجود
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        # ایجاد جدول با نام main_table اگر وجود نداشته باشد
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS main_table (
                id INTEGER PRIMARY KEY,
                set_temperature_1 INT,
                set_humidity_1 INT,
                set_temperature_2 INT,
                set_humidity_2 INT,
                set_temperature_3 INT,
                set_humidity_3 INT,
                set_ip TEXT,
                phone_number_1 TEXT,
                phone_number_2 TEXT,
                phone_number_3 TEXT,
                database_path TEXT
            )
        ''')

        # ذخیره تغییرات و بستن اتصال
        conn.commit()
        conn.close()

    def insert_data(self, set_temperature_1, set_humidity_1, set_temperature_2, set_humidity_2, set_temperature_3,
                    set_humidity_3, set_ip, phone_number_1, phone_number_2, phone_number_3, database_path):
        # ایجاد یک اتصال به دیتابیس
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        # افزودن اطلاعات به دیتابیس
        cursor.execute('''
            INSERT INTO main_table (
                set_temperature_1, set_humidity_1,
                set_temperature_2, set_humidity_2,
                set_temperature_3, set_humidity_3,
                set_ip, phone_number_1,
                phone_number_2, phone_number_3,
                database_path
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (set_temperature_1, set_humidity_1, set_temperature_2, set_humidity_2, set_temperature_3,
              set_humidity_3, set_ip, phone_number_1, phone_number_2, phone_number_3, database_path))

        # ذخیره تغییرات و بستن اتصال
        conn.commit()
        conn.close()

    def update_data(self, id, set_temperature_1, set_humidity_1, set_temperature_2, set_humidity_2, set_temperature_3,
                    set_humidity_3, set_ip, phone_number_1, phone_number_2, phone_number_3, database_path):
        # ایجاد یک اتصال به دیتابیس
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        # به‌روزرسانی اطلاعات در دیتابیس
        cursor.execute('''
            UPDATE main_table
            SET set_temperature_1 = ?,
                set_humidity_1 = ?,
                set_temperature_2 = ?,
                set_humidity_2 = ?,
                set_temperature_3 = ?,
                set_humidity_3 = ?,
                set_ip = ?,
                phone_number_1 = ?,
                phone_number_2 = ?,
                phone_number_3 = ?,
                database_path = ?
            WHERE id = ?
        ''', (set_temperature_1, set_humidity_1, set_temperature_2, set_humidity_2, set_temperature_3,
              set_humidity_3, set_ip, phone_number_1, phone_number_2, phone_number_3, database_path, id))

        # ذخیره تغییرات و بستن اتصال
        conn.commit()
        conn.close()

    def delete_data(self, id):
        # ایجاد یک اتصال به دیتابیس
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        # حذف اطلاعات از دیتابیس
        cursor.execute('DELETE FROM main_table WHERE id = ?', (id,))

        # ذخیره تغییرات و بستن اتصال
        conn.commit()
        conn.close()

    def read_data(self):
        # ایجاد یک اتصال به دیتابیس
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        # خواندن اطلاعات از دیتابیس
        cursor.execute('SELECT * FROM main_table')
        data = cursor.fetchall()

        # بستن اتصال
        conn.close()

        return data
    
    def check_data_existence(self, id):
        # ایجاد یک اتصال به دیتابیس
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        # بررسی وجود داده با شناسه مورد نظر
        cursor.execute('SELECT * FROM main_table WHERE id = ?', (id,))
        
        # خواندن یک رکورد از نتیجه
        result = cursor.fetchone()

        # بستن اتصال
        conn.close()

        # اگر نتیجه وجود داشته باشد، داده وجود دارد
        return result is not None











class current_db:
    def __init__(self, db_name='current_database.db'):
        self.db_name = db_name

    def create_database(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS main_table (
                id INTEGER PRIMARY KEY,
                current_temp1 TEXT  DEFAULT '--',
                current_temp2 TEXT  DEFAULT '--',
                current_temp3 TEXT  DEFAULT '--',
                current_temp4 TEXT  DEFAULT '--',
                current_hum1 TEXT  DEFAULT '--',
                current_hum2 TEXT  DEFAULT '--',
                split INT DEFAULT 5,
                light INT DEFAULT 5,
                generator INT DEFAULT 5,
                smoke INT DEFAULT 5,
                motion INT DEFAULT 5,
                door INT DEFAULT 5,
                voltage_1 TEXT  DEFAULT '--',
                voltage_2 TEXT  DEFAULT '--',
                voltage_3 TEXT  DEFAULT '--',
                current_1 TEXT  DEFAULT '--',
                current_2 TEXT  DEFAULT '--',
                current_3 TEXT  DEFAULT '--',
                air TEXT  DEFAULT '--',
                phase_1 INT DEFAULT 5,
                phase_2 INT DEFAULT 5,
                phase_3 INT DEFAULT 5
            )
        ''')
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        cursor.execute('SELECT COUNT(*) FROM main_table')
        count = cursor.fetchone()[0]

        if count == 0:  # اگر دیتابیس خالی بود
            cursor.execute('''
                INSERT INTO main_table DEFAULT VALUES
            ''')
        conn.commit()
        conn.close()

    def insert_data(self, current_temp1, current_temp2, current_temp3, current_temp4, current_hum1, current_hum2,
                    split, light, generator, smoke, motion, door, voltage_1, voltage_2, voltage_3, current_1,
                    current_2, current_3, air, phase_1, phase_2, phase_3):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO main_table (
                current_temp1, current_temp2, current_temp3, current_temp4, current_hum1, current_hum2,
                split, light, generator, smoke, motion, door, voltage_1, voltage_2, voltage_3, current_1,
                current_2, current_3, air, phase_1, phase_2, phase_3
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (current_temp1, current_temp2, current_temp3, current_temp4, current_hum1, current_hum2,
              split, light, generator, smoke, motion, door, voltage_1, voltage_2, voltage_3, current_1,
              current_2, current_3, air, phase_1, phase_2, phase_3))

        conn.commit()
        conn.close()

    def update_data(self, id, current_temp1, current_temp2, current_temp3, current_temp4, current_hum1, current_hum2,
                    split, light, generator, smoke, motion, door, voltage_1, voltage_2, voltage_3, current_1,
                    current_2, current_3, air, phase_1, phase_2, phase_3):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        cursor.execute('''
            UPDATE main_table
            SET current_temp1 = ?,
                current_temp2 = ?,
                current_temp3 = ?,
                current_temp4 = ?,
                current_hum1 = ?,
                current_hum2 = ?,
                split = ?,
                light = ?,
                generator = ?,
                smoke = ?,
                motion = ?,
                door = ?,
                voltage_1 = ?,
                voltage_2 = ?,
                voltage_3 = ?,
                current_1 = ?,
                current_2 = ?,
                current_3 = ?,
                air = ?,
                phase_1 = ?,
                phase_2 = ?,
                phase_3 = ?
            WHERE id = ?
        ''', (current_temp1, current_temp2, current_temp3, current_temp4, current_hum1, current_hum2,
              split, light, generator, smoke, motion, door, voltage_1, voltage_2, voltage_3, current_1,
              current_2, current_3, air, phase_1, phase_2, phase_3, id))

        conn.commit()
        conn.close()

    def delete_data(self, id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        cursor.execute('DELETE FROM main_table WHERE id = ?', (id,))

        conn.commit()
        conn.close()

    def read_data(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM main_table')
        data = cursor.fetchall()

        conn.close()

        return data

    def check_data_existence(self, id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM main_table WHERE id = ?', (id,))
        
        result = cursor.fetchone()

        conn.close()

        return result is not None
    
    

smart_home_db = SmartHomeDatabase()
smart_home_db.create_database()

current__db=current_db()
current__db.create_database()

# smart_home_db.create_database()
# # smart_home_db.insert_data('25.0', '50.0', '26.0', '55.0', '24.0', '48.0', '192.168.1.1', '123456789', '987654321', '555555555', '/path/to/database')
# smart_home_db.update_data(1, '264444.0', '54442.0', '27.0', '58.0', '25.0', '50.0', '192.168.1.2', '111111111', '222222222', '333333333', '/new/path/to/database')
# data = smart_home_db.read_data()
# print("Data in the database:")
# print(data)



# exists = smart_home_db.check_data_existence(1)

# if exists:
#     print("Data with ID 1 exists.")
# else:
#     print("Data with ID 1 does not exist.")

