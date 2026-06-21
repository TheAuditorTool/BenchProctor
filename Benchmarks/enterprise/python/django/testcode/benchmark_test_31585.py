# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest31585(request):
    xml_value = request.body.decode('utf-8')
    parts = str(xml_value).split(',')
    data = ','.join(parts)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
