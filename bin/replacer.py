#!/usr/bin/python

import subprocess as sp
import os.path
from os import path

SPLUNK_HOME = os.environ['SPLUNK_HOME']
FNAME = "{}/lib/python2.7/site-packages/splunk/appserver/mrsparkle/lib/error.py".format(SPLUNK_HOME)

# Back up the existing `error.py` file if it doesn't already exist
def backup_file():
    if not path.isfile(FNAME):
        print("[*] Backing up your 'error.py' file first. We're silly, not stupid.")
        sp.Popen("/bin/cp {} {}.backup".format(FNAME, FNAME))

def replace_with_image(img_url):
    with open(FNAME, 'r') as infile:
        with open("{}.tmp".format(FNAME), 'w') as outfile:
            ignore_toggle = False
            write_once_toggle = True
            for line in infile:
                tmp = line.strip()
                if tmp.startswith('<svg'):
                    ignore_toggle = True
                if tmp.startswith('</svg'):
                    ignore_toggle = False
                    continue
                if not ignore_toggle:
                    outfile.write(line.rstrip() + '\n')
                if ignore_toggle and write_once_toggle:
                    outfile.write("<img src={}></img>\n".format(img_url))
                    write_once_toggle = False
    print("[*] Replacing your 'error.py' file now!")
    sp.Popen("/bin/mv {}.tmp {}".format(FNAME, FNAME), shell=True)

if __name__ == "__main__":
    backup_file()
    replace_with_image("https://i.imgur.com/5Jl3YWu.jpg")
