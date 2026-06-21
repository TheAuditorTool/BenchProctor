# SPDX-License-Identifier: Apache-2.0
import subprocess
import shlex
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest53189():
    multipart_value = request.form.get('multipart_field', '')
    ns = SimpleNamespace(payload=multipart_value)
    data = getattr(ns, 'payload')
    processed = shlex.quote(data)
    subprocess.run('echo ' + str(processed), shell=True)
    return jsonify({"result": "success"})
