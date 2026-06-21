# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from flask import request


def BenchmarkTest68693():
    xml_value = request.get_data(as_text=True)
    data = str(xml_value).replace('\x00', '')
    return redirect(str(data))
