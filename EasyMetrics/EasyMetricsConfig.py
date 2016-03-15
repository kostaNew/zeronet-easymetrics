import numpy as np

class EasyMetricsConfig(object):

    def __init__(self):
        # General parameters
        self.version = "0.0.4"
        self.time_gap = 30        # Time before start writing
        self.timestep = 60        # Time between writing
        self.folder = "metrics"
        self.params_data_file = "params.json"

        # Zites data
        self.is_write_zite_data = True
        self.zite_data_file = "zites.csv"


easy_metrics_config = EasyMetricsConfig()
