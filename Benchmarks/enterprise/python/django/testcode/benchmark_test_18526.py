# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest18526(request):
    xml_value = request.body.decode('utf-8')
    if xml_value:
        data = xml_value
    else:
        data = ''
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
