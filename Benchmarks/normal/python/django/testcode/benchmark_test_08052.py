# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest08052(request):
    xml_value = request.body.decode('utf-8')
    data = '{}'.format(xml_value)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
