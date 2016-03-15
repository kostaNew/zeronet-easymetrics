from Plugin import PluginManager

import logging
import gevent
import time
import numpy as np
import pandas as pd
from gevent import Greenlet
from EasyMetricsConfig import easy_metrics_config
from EasyMetricsWriter import EasyMetricsWriter
import os

allow_reload = False  # No reload supported

log = logging.getLogger("EasyMetricsPlugin")

@PluginManager.registerTo("Actions")
class ActionsPlugin(object):

    def initialization(self):
        self.config = easy_metrics_config
        self.writer = EasyMetricsWriter()

    def main(self):
        PluginManager.plugin_manager.log.debug("Plugin ZeroMetrics attach to main")
        self.initialization()

        if self.config.is_write_zite_data:
            self.write_zite_data_greenlet = Greenlet.spawn(self.zite_data_greenlet)

        super(ActionsPlugin, self).main()

    def zite_data_greenlet(self):
        gevent.sleep(self.config.time_gap)
        log.debug("The site_data greenlet begin writing the site information")

        while True:
            try:
                from Site import SiteManager
                zites = SiteManager.site_manager.list().values()

                time_ = time.strftime("%Y-%m-%d_%H-%M-%S", time.gmtime())

                time_series = []
                zite_address_series = []
                peers_connected_series = []
                peers_good_series = []
                peers_total_series = []
                content_count_series = []
                out_series = []
                in_series = []

                for zite in zites:
                    zite_address     = zite.address
                    peers_connected  = len([peer for peer in zite.peers.values() if peer.connection and peer.connection.connected])
                    peers_good       = len(zite.getConnectablePeers(100))
                    peers_total      = len(zite.peers)
                    content_count    = len(zite.content_manager.contents)
                    out              = int(zite.settings.get("bytes_sent", 0))
                    in_              = int(zite.settings.get("bytes_recv", 0))

                    time_series.append(time_)
                    zite_address_series.append(zite_address)
                    peers_connected_series.append(peers_connected)
                    peers_good_series.append(peers_good)
                    peers_total_series.append(peers_total)
                    content_count_series.append(content_count)
                    out_series.append(out)
                    in_series.append(in_)

                new_frame = pd.DataFrame(data={'time': time_series,
                                               'address': zite_address_series,
                                               'peers_connected': peers_connected_series,
                                               'peers_good': peers_good_series,
                                               'peers_total': peers_total_series,
                                               'content_count' :content_count_series,
                                               'out': out_series,
                                               'in': in_series},
                                         columns=['time', 'address', 'peers_connected', 'peers_good',
                                                  'content_count', 'out', 'in'])


                self.writer.write_zite_data(new_frame)
            except Exception:
                log.info('The site data information storage round has been FAILED!', exc_info=True)
            else:
                log.info('The site data information storage round has been success')

            gevent.sleep(self.config.timestep)