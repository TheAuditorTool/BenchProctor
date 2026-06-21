# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest38025():
    multipart_value = request.form.get('multipart_field', '')
    data = '%s' % (multipart_value,)
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
