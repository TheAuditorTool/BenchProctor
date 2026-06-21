# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest63028(request):
    xml_value = request.body.decode('utf-8')
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(xml_value))
    return resp
