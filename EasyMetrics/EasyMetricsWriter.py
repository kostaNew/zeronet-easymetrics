import os
import numpy as np
from EasyMetricsConfig import easy_metrics_config

class EasyMetricsWriter:

    def __init__(self):
        self.config = easy_metrics_config
        self.data_folder = os.path.join(self.config.folder, self.config.site_data_folder)
        if not os.path.exists(self.config.folder):
            os.makedirs(self.config.folder)
        if not os.path.exists(self.data_folder):
            os.makedirs(self.data_folder)

    def write_site_data(self, site_name, new_row):
        file = os.path.join(self.data_folder, site_name)

        with open(file, "a+") as fl:
            np.savetxt(fl, new_row)


