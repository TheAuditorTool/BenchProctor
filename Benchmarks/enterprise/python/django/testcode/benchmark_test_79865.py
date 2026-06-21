# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest79865(request):
    xml_value = request.body.decode('utf-8')
    data = str(xml_value).replace('\x00', '')
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
