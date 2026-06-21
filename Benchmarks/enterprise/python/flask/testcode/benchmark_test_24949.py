# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest24949():
    xml_value = request.get_data(as_text=True)
    data = xml_value if xml_value else 'default'
    return Markup('<img src="' + str(data) + '">')
