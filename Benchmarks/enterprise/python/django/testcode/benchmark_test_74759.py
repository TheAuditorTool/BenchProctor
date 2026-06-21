# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest74759(request):
    upload_name = request.FILES['upload'].name
    data = str(upload_name).replace('\x00', '')
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
