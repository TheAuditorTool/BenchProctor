# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest18891(request):
    xml_value = request.body.decode('utf-8')
    data = xml_value if xml_value else 'default'
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
