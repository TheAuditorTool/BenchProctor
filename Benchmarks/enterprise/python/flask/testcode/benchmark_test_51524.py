# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import subprocess


def BenchmarkTest51524():
    xml_value = request.get_data(as_text=True)
    def normalize(value):
        return value.strip()
    data = normalize(xml_value)
    if data not in ('ls', 'cat', 'date', 'whoami'):
        return jsonify({'error': 'forbidden'}), 403
    processed = data
    subprocess.run([str(processed), '--status'], shell=False)
    return jsonify({"result": "success"})
