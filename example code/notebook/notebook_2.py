# Daytime recording
parquet_file = r'./data/data_synced.parquet'
df = pd.read_parquet(parquet_file)

df_filtered_day = df.drop(['T1E_x', 'T1E_y', 'T1E_z'], axis=1)

df_filtered_day = df.drop(['T1E_x', 'T1E_y', 'T1E_z'], axis=1)
df_filtered_day = df_filtered_day.drop(df.index[0:16*9*3600+30000])
df_filtered_day = df_filtered_day.drop(df.index[-1])
df_filtered_day = df_filtered_day.drop(df.index[16*10*3600:-1])
df_filtered_day.shape