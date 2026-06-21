# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest04425():
    xml_value = request.get_data(as_text=True)
    return Markup('<img src="' + str(xml_value) + '">')
