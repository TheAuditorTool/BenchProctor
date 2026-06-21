# SPDX-License-Identifier: Apache-2.0
from flask import request
from flask import redirect
import urllib.parse


def BenchmarkTest01652():
    xml_value = request.get_data(as_text=True)
    data = xml_value if xml_value else 'default'
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
