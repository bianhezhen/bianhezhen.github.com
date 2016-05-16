# coding=utf-8
import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)


def n():
    logging.debug('Starting')
    # time.sleep(5)
    logging.debug('Exiting')


def d():
    logging.debug('Starting')
    time.sleep(100)
    logging.debug('Exiting')

if __name__ == '__main__':

    t = threading.Thread(name='non-daemon', target=n)

    d = threading.Thread(name='daemon', target=d)
    d.setDaemon(True)
    # t.setDaemon(True)
    d.start()
    t.start()

# python myThread.py
# (daemon) Starting
# (non - daemon) Starting
# (daemon) Exiting
# (non - daemon) Exiting

# Python myThread.py
# (daemon) Starting
# (non - daemon) Starting
# (non - daemon) Exiting
