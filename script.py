from tabula.io import read_pdf

dfs = read_pdf('pdf_sample.pdf' , pages = '2')
for i in range(2):
    dfs[i].to_csv(f'table_{i}.csv' , index = False)
