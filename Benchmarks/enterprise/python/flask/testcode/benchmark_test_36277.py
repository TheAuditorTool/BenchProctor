# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify


def BenchmarkTest36277():
    multipart_value = request.form.get('multipart_field', '')
    data = '%s' % (multipart_value,)
    subprocess.run('echo ' + str(data), shell=True)
    return jsonify({"result": "success"})
