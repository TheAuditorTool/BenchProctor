# SPDX-License-Identifier: Apache-2.0
from django.http import HttpResponse


def BenchmarkTest00130(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = ' '.join(str(referer_value).split())
    resp = HttpResponse(status=302)
    resp['Location'] = str(data)
    return resp
