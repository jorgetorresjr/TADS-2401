from functions.insert_rows import insert_one_row
from functions.create_table import create_table


create_table(
    database='mydatabase',
    table_name='produtos',
    columns_desc="""
        id_produto INTEGER PRIMARY KEY,
        nome CHAR NOT NULL,
        qtd INTEGER NOT NULL
    """
)

insert_one_row(
   database_name='mydatabase',
    table_name='produtos',
    columns_name='nome, qtd',
    values="'Xbox', 90"
)

