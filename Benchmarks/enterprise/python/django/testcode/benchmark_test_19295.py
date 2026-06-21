# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest19295(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = f'{multipart_value:.200s}'
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
