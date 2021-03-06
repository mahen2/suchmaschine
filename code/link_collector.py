# -*- coding: utf-8 -*-
import urllib2
import zipfile
from os import path, pardir

from config import TOP1M_PATH


def get_top_1million_websites(limit=1000000):
    filepath = path.join(pardir, "data", "top-1m.csv.zip")
    # download the file from the web if there is no local file
    if not path.exists(filepath):
        url = TOP1M_PATH
        download = urllib2.urlopen(url).read()
        with open(filepath, "wb") as output:
            output.write(download)
    # unzip the file
    with zipfile.ZipFile(filepath, "r") as top1m_file:
        # parse the file (append "http://www" to every entry and only pass
        # the url)
        top1mCSV = top1m_file.read(
            top1m_file.namelist()[0], "r").split('\n')[:limit]
        return ["http://www." + row.split(",")[1] for row
                in top1mCSV if row != ""]


def get_websites_from_txt(filename):
    filepath = path.join(pardir, "data", filename)
    if path.exists(filepath):
        with open(filepath, 'rb') as uglysites:
            return [line.strip('\n') for line in uglysites.readlines()]


if __name__ == "__main__":
    print len(get_top_1million_websites())
    print len(get_websites_from_txt('uglysites.txt'))
