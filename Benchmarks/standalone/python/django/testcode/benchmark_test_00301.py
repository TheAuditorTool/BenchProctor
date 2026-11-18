# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00301(request):
    field_value = request.POST.get('field', '')
    data = str(field_value).replace('\x00', '')
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
