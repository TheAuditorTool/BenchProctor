# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import time
from types import SimpleNamespace


def BenchmarkTest67729():
    xml_value = request.get_data(as_text=True)
    ns = SimpleNamespace(payload=xml_value)
    data = getattr(ns, 'payload')
    if time.time() > 1000000000:
        with open('/var/uploads/' + str(data), 'wb') as fh:
            fh.write(b'data')
    return jsonify({"result": "success"})
