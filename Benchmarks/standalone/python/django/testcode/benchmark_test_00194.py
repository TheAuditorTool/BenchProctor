# SPDX-License-Identifier: Apache-2.0
from django.http import HttpResponse


def BenchmarkTest00194(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    def normalize(value):
        return value.strip()
    data = normalize(referer_value)
    resp = HttpResponse(status=302)
    resp['Location'] = str(data)
    return resp
