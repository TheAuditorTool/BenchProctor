# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest00913():
    xml_value = request.get_data(as_text=True)
    data = str(xml_value).replace('\x00', '')
    return Markup('<div>' + str(data) + '</div>')
