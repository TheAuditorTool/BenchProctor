# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest64910():
    xml_value = request.get_data(as_text=True)
    data = f'{xml_value}'
    return Markup('<img src="' + str(data) + '">')
