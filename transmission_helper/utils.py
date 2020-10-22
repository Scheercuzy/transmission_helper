import os
import shutil
import errno
import logging

logger = logging.getLogger('transmission_helper.utils')


def copy(src, dst):
    logger.debug("Copying {}".format(os.path.basename(src)))
    try:
        if not os.path.isfile(src):
            dst = os.path.join(dst, os.path.basename(src))
        shutil.copytree(src, dst)
    except OSError as e:
        # If the error was caused because the source wasn't a directory
        if e.errno == errno.ENOTDIR:
            shutil.copy(src, dst)
        else:
            raise Exception('Not copied. Error: %s' % e)
