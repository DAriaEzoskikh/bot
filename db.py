import sqlite3
connect = sqlite3.connect('bd.db')
cursor = connect.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS "users" ("id" Integer not null, "tg_id" Integer not null, primary key("id" AUTOINCREMENT));''')
connect.commit()

cursor.execute('''CREATE TABLE if not exists "categories" (
	"id"	INTEGER NOT NULL UNIQUE,
	"name"	TEXT NOT NULL,
	"value"	TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);''')
connect.commit()

cursor.execute('''CREATE TABLE IF NOT EXISTS "subscribes" ("user_id" Integer not null, "category_id" Integer not null);''')
connect.commit()

i=0
categ_name = ['Спорт', 'Бизнес', 'Развлечения', 'Главное', 'Здоровье', 'Наука', 'Технологии']
categ_value = ['sports', 'business', 'entertainment', 'general', 'health', 'science', 'technology']

while i < len(categ_name):
    cursor.execute('''INSERT INTO categories(name, value) VALUES(?,?)''',    (categ_name[i], categ_value[i]))
    connect.commit()
    i=i+1




