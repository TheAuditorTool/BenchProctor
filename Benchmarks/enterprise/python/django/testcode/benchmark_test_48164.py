# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest48164(request):
    xml_value = request.body.decode('utf-8')
    parts = str(xml_value).split(',')
    data = ','.join(parts)
    request.session.set_expiry(1800)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
