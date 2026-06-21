# SPDX-License-Identifier: Apache-2.0
from flask import redirect
import re
from flask import jsonify
from types import SimpleNamespace


def BenchmarkTest01628(path_param):
    path_value = path_param
    ns = SimpleNamespace(payload=path_value)
    data = getattr(ns, 'payload')
    if not re.fullmatch('^[\\w\\s./\\\\:_?&=\\-@]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return redirect(str(processed))
