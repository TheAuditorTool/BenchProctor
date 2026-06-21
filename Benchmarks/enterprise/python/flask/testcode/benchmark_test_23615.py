# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest23615():
    multipart_value = request.form.get('multipart_field', '')
    data, _sep, _rest = str(multipart_value).partition('\x00')
    os.chmod('/var/app/data/' + str(data), 0o777)
    return jsonify({"result": "success"})
