import numpy as np

class EasyMetricsConfig(object):

    def __init__(self):
        # General parameters
        self.version = "0.0.2"
        self.time_gap = 30        # Time before start writing
        self.timestep = 60        # Time between writing
        self.folder = "metrics"

        # Sites data
        self.is_write_site_data = True
        self.site_data_file = "site.csv"


easy_metrics_config = EasyMetricsConfig()
