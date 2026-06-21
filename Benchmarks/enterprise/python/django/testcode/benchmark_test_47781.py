# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest47781(request):
    xml_value = request.body.decode('utf-8')
    def normalize(value):
        return value.strip()
    data = normalize(xml_value)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
