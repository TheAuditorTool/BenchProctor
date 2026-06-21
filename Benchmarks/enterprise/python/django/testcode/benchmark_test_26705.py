# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest26705(request):
    upload_name = request.FILES['upload'].name
    data = f'{upload_name}'
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
