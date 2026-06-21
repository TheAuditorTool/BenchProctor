# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest72108(request):
    xml_value = request.body.decode('utf-8')
    data = f'{xml_value}'
    request.session.set_expiry(1800)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
