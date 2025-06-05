import pandas as pd
from tabula import read_pdf


path = ''
filename = ''
my_file = f'{path}\{filename}'


tabular_data = read_pdf(
    my_file, 
    pages='all',
    multiple_tables=True,
    lattice=True,
    stream=True,
    guess=False,
    pandas_options={'header': None}
    )

for n, table in enumerate(tabular_data, 1):
    pd.DataFrame(table).iloc[:, :4].to_csv(f'table_{str(n).zfill(3)}.csv')