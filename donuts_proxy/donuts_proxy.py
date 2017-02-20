#!/usr/bin/env python
import dns
import logging
from lib import *

logger = logging.getLogger('donuts-proxy')

def dns_callback(**kwargs):
    for i in kwargs['tokens']:
        logger.info(
            """Updating token: %s"""
        %i)
        api = '%s/?hash=%s&ip=%s' %(kwargs['ws'], i, kwargs['ip'])
        try:
            res = requests.get(api, verify=False)
            logger.debug(
                """%s: just updated (%s) - %s"""
            %(i, kwargs['ip'], res.content))
        except:
            logger.debug(
                """%s: could not been updated (%s)"""
            %(i, kwargs['ip']))
    return True

def run(options):
    print(options)
    
def main():
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("-c", "--config", dest="config",
                      default='/etc/donuts/donuts-proxy.conf',
                      help="Configuration file.", metavar="CONFIG")
    parser.add_option("-d", "--daemon", dest="daemon", default=False,
                      action="store_true",
                      help="Run as a daemon.")
    (options, args) = parser.parse_args()

    with open(options.config, 'r') as ymlfile:
        cfg = yaml.load(ymlfile)
        cfg.setdefault('logfile', '/var/log/donuts-proxy.log')
        cfg.setdefault('loglevel', 'info')
        cfg.setdefault('logformat',
                       """%(asctime)s - %(name)s - %(levelname)s - %(message)s""")
        cfg['daemon']  = options.daemon
        handler = logging.FileHandler(cfg['logfile'])
        handler.setFormatter(logging.Formatter(cfg['logformat'],
                                               "%Y-%m-%d %H:%M:%S"))
        logger.addHandler(handler)
        logger.setLevel(getattr(logging, cfg.get('loglevel').upper()))
    run(cfg)
    
if __name__ == '__main__':
    main()
