# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import request, jsonify


def BenchmarkTest08114():
    referer_value = request.headers.get('Referer', '')
    data = '%s' % (referer_value,)
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
