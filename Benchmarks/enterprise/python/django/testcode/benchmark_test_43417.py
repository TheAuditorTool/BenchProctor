# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest43417(request):
    xml_value = request.body.decode('utf-8')
    data, _sep, _rest = str(xml_value).partition('\x00')
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
