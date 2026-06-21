# SPDX-License-Identifier: Apache-2.0
from flask import request
from flask import redirect
import urllib.parse
from types import SimpleNamespace


def BenchmarkTest04332():
    multipart_value = request.form.get('multipart_field', '')
    ns = SimpleNamespace(payload=multipart_value)
    data = getattr(ns, 'payload')
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
