# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup


def BenchmarkTest00718(path_param):
    path_value = path_param
    data = ' '.join(str(path_value).split())
    return Markup('<img src="' + str(data) + '">')
