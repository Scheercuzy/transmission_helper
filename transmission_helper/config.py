import os
import yaml


class ConfigHandler:
    config_options = [
        {'name': 'user'},
        {'name': 'password'},
        {'name': 'ip', "default": "127.0.0.1"},
        {'name': 'port', "default": 9091},
        {'name': 'src_dir'},
        {'name': 'dst_dir'},
    ]
    default_filename = 'config.yaml'

    def get_config(self):
        return self._get_config_from_yaml()

    def _get_config_from_yaml(self):
        with open(self.default_filename, 'r') as yml:
            return yaml.load(yml, Loader=yaml.FullLoader)

    def _get_config_from_env(self):
        return {
            'user': os.environ.get('USER'),
            'password': os.environ.get('PASSWORD'),
            'ip': os.environ.get('IP'),
            'port': os.environ.get('PORT'),
            'dst_dir': os.environ.get('DST_DIR'),
            'src_dir': os.environ.get('SRC_DIR'),
        }
