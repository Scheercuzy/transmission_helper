import os
import logging

from flask import Flask, request

from transmission_helper import utils
from transmission_helper.config import ConfigHandler


logger = logging.getLogger('transmission_helper.webserver')


app = Flask(__name__)
config_handler = ConfigHandler()


@app.route('/', methods=['GET'])
def index():
    return "Transmission Helper Webserver is running correctly"


@app.route("/torrent_complete", methods=['POST'])
def torrent_complete():
    data = request.get_json()

    if data is None:
        return {
            "error": "Make sure your request is in json format or has the \
                correct header for content type 'application/json'"
        }

    if 'torrent_name' not in data:
        return {
            "error": "torrent_name is required"
        }

    torrent_name = data['torrent_name']

    config = config_handler.get_config()

    utils.copy(
        os.path.join(config['src_dir'], torrent_name),
        config['dst_dir'])
    logger.info("{} copied".format(torrent_name))

    return 'Success'


if __name__ == '__main__':
    app.run(port=5050)
