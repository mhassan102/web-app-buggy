import os
import tarfile

from flask import abort, request


def unpack():
    upload = request.files.get("archive")
    if upload is None:
        abort(400)
    path = os.path.join("/tmp", "buggy-upload.tar")
    upload.save(path)
    destination = "/tmp/buggy-unpacked"
    os.makedirs(destination, exist_ok=True)
    with tarfile.open(path) as bundle:
        bundle.extractall(destination, filter="fully_trusted")  # BUG: tarslip — archive member names are extracted without a destination check
    return "unpacked"
