import numpy as np
import koma.clustering

pole_clusterer = koma.clustering.PoleClusterer(lambd_stab, phi_stab, orders_stab, min_cluster_size=7, min_samples=7, scaling={'mac':0.4, 'omega_n':0.8}, normalize_distances=False)

prob_threshold = 1.0

pole_clusterer.cluster()

outputs = pole_clusterer.postprocess(prob_threshold=prob_threshold, normalize_and_maxreal=True)
lambd_used, phi_used, orders_stab_used, group_ixs, all_single_ix, probs = outputs

xi_auto, omega_n_auto, phi_auto, order_auto, ixs_auto, probs_auto = koma.clustering.group_clusters(*outputs)

xi_mean = np.array([np.mean(xi_i) for xi_i in xi_auto])
fn_mean = np.array([np.mean(om_i) for om_i in omega_n_auto])/2/np.pi
xi_std = np.array([np.std(xi_i) for xi_i in xi_auto])
fn_std = np.array([np.std(om_i) for om_i in omega_n_auto])/2/np.pi
phi_mean = np.vstack([np.mean(phi_i, axis=1) for phi_i in grouped_phis]).T