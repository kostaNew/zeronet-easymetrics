import numpy as np

class EasyMetricsConfig(object):

    def __init__(self):
        # General parameters
        self.version = "0.0.1"
        self.time_gap = 30        # Time before start writing
        self.timestep = 60        # Time between writing
        self.folder = "metrics"

        # Site data
        self.is_write_site_data = True
        self.site_data_folder = "site"
        self.site_data_template = np.dtype([('time', float), ('peers_connected', int), ('peers_good', int), ('peers_total', int)])


easy_metrics_config = EasyMetricsConfig()
