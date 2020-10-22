import logging

logger = logging.getLogger('transmission_helper')
logger.setLevel(logging.DEBUG)

fh = logging.FileHandler('transmission_helper.log')
fh.setLevel(logging.INFO)

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

file_format = logging.Formatter(
    '%(asctime)s - %(levelname)s:%(message)s')
console_format = logging.Formatter(
    '%(message)s')

ch.setFormatter(console_format)
fh.setFormatter(file_format)

logger.addHandler(ch)
logger.addHandler(fh)
