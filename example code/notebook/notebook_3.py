# Detrending
acceleration_data_day = df_filtered_day.to_numpy()
acceleration_data_night = df_filtered_night.to_numpy()

fs = 16
t_day = np.arange(0, len(acceleration_data_day))
t_s_day = t_day / fs

t_night = np.arange(0, len(acceleration_data_night))
t_s_night = t_night / fs

acceleration_data_day = scs.detrend(acceleration_data_day, axis=0)
acceleration_data_night = scs.detrend(acceleration_data_night, axis=0)