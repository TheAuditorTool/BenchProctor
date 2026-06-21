# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import request, jsonify


def BenchmarkTest06773():
    multipart_value = request.form.get('multipart_field', '')
    data = '%s' % (multipart_value,)
    yaml.safe_load(data)
    return jsonify({"result": "success"})
