import os
import pandas as pd
from tabula import read_pdf

from data import pathtofile, chapter_names



filename = os.path.join(*pathtofile, f'{chapter_names[0]}.pdf')



tabular_data = read_pdf(
    filename, 
    pages='all',
    multiple_tables=True,
    lattice=True,
    stream=True,
    guess=False,
    pandas_options={'header': None}
    )


# print(f'Number tables: {len(tabular_data)}')
print(tabular_data[2])

# for n, table in enumerate([tabular_data[0], tabular_data[1], tabular_data[5]], 1):
#     (
#         pd.DataFrame(table)
#         .iloc[:, 1:-1]
#         .to_csv(
#             f'{chapter_names[0]}_{str(n).zfill(3)}.csv', 
#             index=False, 
#             # encoding='latin-1',
#             )
#         )