import os
import sys
import getopt
from flowci import client

api = client.Client()
uploaded = set()

def startFromInput(path):
    for line in path.splitlines():
        for item in line.split(";"):
            if item == '' or not os.path.exists(item):
                log("path or file '%s' not found" % item)
                continue

            if os.path.isfile(item):
                uploadFile(item)
                continue

            if os.path.isdir(item):
                uploadDir(item)


def uploadFile(path, srcDir = None):
    if path in uploaded:
        return

    uploaded.add(path)
    log("file '%s' will be loaded.." % path)
    r = api.uploadJobArtifact(path, srcDir)
    log("upload status is %s" % r)


def uploadDir(path, parent = ''):
    dirName = os.path.join(parent, os.path.basename(path))

    for i in os.listdir(path):
        fullPath = os.path.join(path, i)
        
        if os.path.isfile(fullPath):
            uploadFile(fullPath, dirName)
            continue

        if os.path.isdir(fullPath):
            uploadDir(fullPath, dirName)


def log(msg):
    print("[artifact-upload]: " + msg)


# start
inputStr = sys.argv[1]
startFromInput(inputStr)
