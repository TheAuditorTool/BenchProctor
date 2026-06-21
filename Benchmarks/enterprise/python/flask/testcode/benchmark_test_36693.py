# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest36693():
    upload_name = request.files['doc'].filename
    data = '%s' % (upload_name,)
    with open('/var/app/data/' + str(data), 'w') as fh:
        fh.write('data')
    return jsonify({"result": "success"})
