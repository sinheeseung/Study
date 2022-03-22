import pandas as pd
import pandas_profiling
import tensorflow as tf

data = pd.read_csv(r'D:\신희승\Study\NLP\pandas_profiling\spam.csv', encoding = 'latin1')

pr = data.profile_report()

pr.to_file('./pr_report.html')


