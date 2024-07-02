import pandas as pd 
import numpy as np

def dataClean(path: str, sheet: str) -> pd.DataFrame:
    data = pd.read_excel(path, sheet_name=None)
    df = data[sheet]
    
    keep = ['placement', 'name', 'time', 'team', 'year', 'conference', 'placement.4', 'region', 'placement.5', 'prior NCAA place']
    df = df[keep]
    temp = df.rename(columns={'placement': 'ncaaPlace', 'placement.4': 'conferencePlace', 'placement.5': 'regionPlace', 'prior NCAA place': 'ncaaPriorPlace', 'time': 'ncaaTime'}, inplace=False)
    df = temp
    
    df.fillna('n/a', inplace=True)
    def ordinal_to_int(ordinal_str):
        if ordinal_str == 'n/a':
            return np.nan
        return int(''.join(filter(str.isdigit, ordinal_str)))

    df['conferencePlace'] = df['conferencePlace'].apply(ordinal_to_int)
    df['regionPlace'] = df['regionPlace'].apply(ordinal_to_int)
    df['ncaaPriorPlace'] = df['ncaaPriorPlace'].apply(ordinal_to_int)

    return df