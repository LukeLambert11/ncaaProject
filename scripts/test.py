import pandas
df = pandas.read_excel('/Users/lukelambert/Desktop/NCAA_XC.xlsx', sheet_name=['Women 2018'])

import pandas
df = pandas.read_excel('/Users/lukelambert/Desktop/NCAA_XC.xlsx', sheet_name=['Women 2018'])



# Display all columns
pandas.set_option('display.max_rows', None)


print(df)