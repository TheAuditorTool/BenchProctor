# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import request, jsonify


def BenchmarkTest04482():
    referer_value = request.headers.get('Referer', '')
    data = '%s' % str(referer_value)
    yaml.safe_load(data)
    return jsonify({"result": "success"})
