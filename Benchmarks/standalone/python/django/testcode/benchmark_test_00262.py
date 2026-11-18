# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import unquote


def BenchmarkTest00262(request):
    field_value = request.POST.get('field', '')
    data = unquote(field_value)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), httponly=True, samesite='Strict')
    return resp
