# SPDX-License-Identifier: Apache-2.0
from django.utils.safestring import mark_safe
from django.http import HttpResponse


def BenchmarkTest00161(request, path_param):
    path_value = path_param
    data = '{}'.format(path_value)
    return HttpResponse(mark_safe('<div>' + str(data) + '</div>'))
