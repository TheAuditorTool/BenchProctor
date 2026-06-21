# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest35945():
    multipart_value = request.form.get('multipart_field', '')
    data = ' '.join(str(multipart_value).split())
    os.chmod('/var/app/data/' + str(data), 0o777)
    return jsonify({"result": "success"})
