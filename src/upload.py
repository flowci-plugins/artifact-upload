import os
from flowci import client

api = client.Client()


def start(path):
    items = path.split(";")

    for item in items:
        if item == '' or not os.path.exists(item):
            continue

        if os.path.isfile(item):
            uploadFile(item)
            continue

        if os.path.isdir(item):
            uploadDir(item)


def uploadFile(path, srcDir = None):
    r = api.uploadJobArtifact(path, srcDir)
    log("file %s upload status is %s" % (path, r))


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


inPath = client.GetVar("FLOWCI_JOB_ARTIFACT_PATH")
start(inPath)
