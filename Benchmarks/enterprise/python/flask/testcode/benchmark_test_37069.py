# SPDX-License-Identifier: Apache-2.0
from flask import request
from flask import redirect
import urllib.parse


def coalesce_blank(value):
    return value or ''

def BenchmarkTest37069():
    raw_body = request.get_data(as_text=True)
    data = coalesce_blank(raw_body)
    processed = data[:64]
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(processed))
    return redirect(target)
