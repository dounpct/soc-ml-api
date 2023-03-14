import pandas as pd

def maskThreat(df):
    toThreatHourStr = '08:00:00.000'
    fromThreatHourStr = '17:00:00.000'
    # countryStr = ["Russian Federation","Slovakia","China","Netherlands","Thailand"]
    countryStr = ["Russian Federation"]
    return df.assign(is_threat=pd.Series('no', index=df.index).mask(((df['mt.ads_country_dst'].isin(countryStr)) & ((df['@timestamp'].str[-12:]<toThreatHourStr) | (df['@timestamp'].str[-12:]>fromThreatHourStr))), 'yes'))

def maskOfficeHour(df):
    fromHourStr = '08:00:00.000'
    toHourStr = '17:00:00.000'
    return df.assign(is_OfficeHour=pd.Series('no', index=df.index).mask((((df['@timestamp'].str[-12:]>=fromHourStr) & (df['@timestamp'].str[-12:]<=toHourStr))), 'yes'))
