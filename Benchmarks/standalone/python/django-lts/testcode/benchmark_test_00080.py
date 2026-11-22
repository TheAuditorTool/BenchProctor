# SPDX-License-Identifier: Apache-2.0
from django.http import HttpResponse


def BenchmarkTest00080(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data, _sep, _rest = str(forwarded_ip).partition('\x00')
    resp = HttpResponse(content_type='text/html')
    resp.write('<div>' + str(data) + '</div>')
    return resp
