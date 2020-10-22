import logging

import transmissionrpc
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.executors.pool import ThreadPoolExecutor

from transmission_helper.config import ConfigHandler


logger = logging.getLogger('transmission_helper')

confighandler = ConfigHandler()


def remove_finished_torrents():
    config = confighandler.get_config()
    logger.debug("Connecting to transmission...")
    tc = transmissionrpc.Client(
        config['ip'],
        config['port'],
        config['user'],
        config['password'])
    logger.debug("Connected!")
    for torrent in tc.get_torrents():
        if torrent.isFinished:
            tc.remove_torrent(torrent.id, delete_data=True)
            logger.info("{} removed".format(torrent.name))


def main():
    executors = {
        'default': ThreadPoolExecutor(1)
    }
    scheduler = BlockingScheduler(executors=executors)
    scheduler.add_job(remove_finished_torrents, 'interval', minutes=15)
    logger.info("Starting Scheduler")
    scheduler.start()


if __name__ == "__main__":
    main()
