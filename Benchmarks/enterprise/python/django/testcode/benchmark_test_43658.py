# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest43658(request):
    xml_value = request.body.decode('utf-8')
    def normalize(value):
        return value.strip()
    data = normalize(xml_value)
    request.session.set_expiry(1800)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
