# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00550(request):
    field_value = request.POST.get('field', '')
    data = f'{field_value!s}'
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), httponly=True, samesite='Strict')
    return resp
