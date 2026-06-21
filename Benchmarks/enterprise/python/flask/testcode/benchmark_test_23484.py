# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os
import tempfile


def normalise_input(value):
    return value.strip()

def BenchmarkTest23484():
    xml_value = request.get_data(as_text=True)
    data = normalise_input(xml_value)
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    os.chmod(path, 0o777)
    return jsonify({"result": "success"})
