# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def to_text(value):
    return str(value).strip()

def BenchmarkTest34220(request):
    upload_name = request.FILES['upload'].name
    data = to_text(upload_name)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
