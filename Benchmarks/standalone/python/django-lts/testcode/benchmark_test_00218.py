# SPDX-License-Identifier: Apache-2.0
import html
from django.http import HttpResponse


def BenchmarkTest00218(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = '%s' % (referer_value,)
    processed = html.escape(data)
    resp = HttpResponse(content_type='text/html')
    resp.write('<div>' + str(processed) + '</div>')
    return resp
