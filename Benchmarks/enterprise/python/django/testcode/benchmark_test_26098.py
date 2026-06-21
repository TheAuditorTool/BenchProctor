# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def relay_value(value):
    return value

def BenchmarkTest26098(request):
    upload_name = request.FILES['upload'].name
    data = relay_value(upload_name)
    if str(data).lower() not in ('true', 'false'):
        return JsonResponse({'error': 'invalid boolean'}, status=400)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
