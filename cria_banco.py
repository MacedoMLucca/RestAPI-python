import sqlite3

connection = sqlite3.connect('banco.db')
cursor = connection.cursor()

cria_tabela = "CREATE TABLE IF NOT EXISTS hoteis(hotel_id text PRIMARY KEY,\
                                                nome text, diaria real, cidade text)"
atualiza_tabela = "ALTER TABLE hoteis ADD estrelas real AFTER nome"

cria_hotel = "INSERT INTO hoteis VALUES ('alpha','alpha Hotel', 4.3, 345.30,'Rio de janeiro')"

cursor.execute(cria_tabela)
cursor.execute(atualiza_tabela)
cursor.execute(cria_hotel)

connection.commit()
connection.close()
