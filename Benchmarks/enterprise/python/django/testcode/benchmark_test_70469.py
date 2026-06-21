# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest70469(request):
    upload_name = request.FILES['upload'].name
    data = f'{upload_name:.200s}'
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
