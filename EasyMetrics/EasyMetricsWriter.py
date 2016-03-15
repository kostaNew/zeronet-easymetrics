import os
import time
import json
import numpy as np
from EasyMetricsConfig import easy_metrics_config

class EasyMetricsWriter:

    def __init__(self):
        self.config = easy_metrics_config
        self.directory_name = time.strftime("%Y-%m-%d_%H-%M-%S", time.gmtime())

        self.is_header_need_set = True

        self.data_folder = os.path.join(self.config.folder, self.directory_name)
        if not os.path.exists(self.config.folder):
            os.makedirs(self.config.folder)
        if not os.path.exists(self.data_folder):
            os.makedirs(self.data_folder)

        params_file = os.path.join(self.data_folder, self.config.params_data_file)

        with open(params_file, 'w') as outfile:
            json.dump(self.config.__dict__, outfile)


    def write_zite_data(self, new_frame):
        file = os.path.join(self.data_folder, self.config.zite_data_file)

        with open(file, "a+") as fl:
           new_frame.to_csv(fl, index=False, header=self.is_header_need_set)
           self.is_header_need_set = False


