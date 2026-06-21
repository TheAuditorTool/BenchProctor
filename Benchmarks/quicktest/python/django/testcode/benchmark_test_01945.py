# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest01945(request):
    upload_name = request.FILES['upload'].name
    data = upload_name if upload_name else 'default'
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
