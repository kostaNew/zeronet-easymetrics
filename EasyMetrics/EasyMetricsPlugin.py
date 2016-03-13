from Plugin import PluginManager

import logging
import gevent
import time
import numpy as np
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

        if self.config.is_write_site_data:
            self.write_site_data_greenlet = Greenlet.spawn(self.site_data_greenlet)

        super(ActionsPlugin, self).main()

    def site_data_greenlet(self):
        gevent.sleep(self.config.time_gap)
        log.debug("The site_data greenlet begin writing the site information")

        while True:
            try:
                from Site import SiteManager
                sites = SiteManager.site_manager.list()
                for site in sorted(sites.values(), lambda a, b: cmp(a.address, b.address)):
                    time_ = time.time()
                    peers_connected = len([peer for peer in site.peers.values() if peer.connection and peer.connection.connected])
                    peers_good = len(site.getConnectablePeers(100))
                    peers_total = len(site.peers)
                    new_row = np.array([(time_, peers_connected, peers_good, peers_total)], dtype=self.config.site_data_template)
                    self.writer.write_site_data(site.address, new_row)
            except Exception:
                log.info('The site data information storage round has been FAILED!', exc_info=True)
            else:
                log.info('The site data information storage round has been success')

            gevent.sleep(self.config.timestep)