# SPDX-License-Identifier: Apache-2.0
import bleach
from django.http import HttpResponse


def BenchmarkTest00218(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data, _sep, _rest = str(referer_value).partition('\x00')
    processed = bleach.clean(data)
    resp = HttpResponse(content_type='text/html')
    resp.write('<div>' + str(processed) + '</div>')
    return resp
