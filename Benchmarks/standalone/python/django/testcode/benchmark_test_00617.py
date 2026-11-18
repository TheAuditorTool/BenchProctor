# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00617(request):
    xml_value = request.body.decode('utf-8')
    data = f'{xml_value!s}'
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
