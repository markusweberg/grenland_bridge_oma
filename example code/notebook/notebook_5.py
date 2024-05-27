# CoV-SSI
i = 200
order = np.arange(2, 62, 2)
fs = 16

lambd, phi, orders = koma.oma.covssi(acceleration_data_day, fs, i, order, return_flat=True)

# Stabilisation
stabcrit = {'freq':0.05, 'damping':0.2, 'mac':0.1}
s = 2
valid_range = {'freq':[0, np.inf], 'damping':[0, 0.3], 'mpc':[0.6, 1]}

lambd_stab, phi_stab, orders_stab, ix_stab = koma.oma.find_stable_poles(lambd, phi, orders, s, stabcrit=stabcrit, valid_range=valid_range, indicator='freq', use_legacy=False)