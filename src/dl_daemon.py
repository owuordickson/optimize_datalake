# -*- coding: utf-8 -*-
"""
@author: "Marziye Derakhshannia and Dickson Owuor"
@credits: "Anne Laurent"
@license: "MIT"
@version: "1.0"
@email: "dm.derakhshannia@gmail.com or owuordickson@gmail.com "
@created: "26 October 2020"

Usage:
    $python3 init_dlopt.py -f ../data/test_file.csv
Description:
    f -> file path (CSV)

"""

import sys
from algorithms.dolpt.dlopt import DlOpt


def write_file(data, path):
    with open(path, 'w') as f:
        f.write(data)
        f.close()


if __name__ == "__main__":
    daemon = DlOpt('/tmp/daemon-example.pid')
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            daemon.start()
        elif 'stop' == sys.argv[1]:
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            daemon.restart()
        else:
            print("Unknown command")
            sys.exit(2)
        sys.exit(0)
    else:
        print("usage: %s start|stop|restart" % sys.argv[0])
        sys.exit(2)
