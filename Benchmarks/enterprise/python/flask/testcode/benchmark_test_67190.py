# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from flask import request, jsonify


def BenchmarkTest67190():
    raw_body = request.get_data(as_text=True)
    data = '%s' % (raw_body,)
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
