# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import redirect
import urllib.parse


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest17971():
    raw_body = request.get_data(as_text=True)
    reader = make_reader(raw_body)
    data = reader()
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(processed))
    return redirect(target)
