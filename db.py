import sqlite3
connect = sqlite3.connect('bd.db')
cursor = connect.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS "users" ("id" Integer not null, "tg_id" Integer not null, primary key("id" AUTOINCREMENT));''')
connect.commit()
cursor.execute('''CREATE TABLE IF NOT EXISTS "categories" ("id" Integer not null, "name" Text not null, primary key("id" AUTOINCREMENT));''')
connect.commit()
categ_name = ['Спорт', 'Бизнес', 'Развлечения', 'Главное', 'Здоровье', 'Наука', 'Технологии']
categ_value = ['sports', 'business', 'entertainment', 'general', 'health', 'science', 'technology']

cursor.execute('''CREATE TABLE IF NOT EXISTS "subscribes" ("user_id" Integer not null, "category_id" Integer not null);''')
connect.commit()

