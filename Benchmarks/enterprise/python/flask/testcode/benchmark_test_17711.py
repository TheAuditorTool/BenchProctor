# SPDX-License-Identifier: Apache-2.0
from flask import request
from types import SimpleNamespace


def BenchmarkTest17711():
    field_value = request.form.get('field', '')
    ns = SimpleNamespace(payload=field_value)
    data = getattr(ns, 'payload')
    processed = data[:64]
    with open('/var/app/data/' + str(processed), 'r') as fh:
        content = fh.read()
    return content
