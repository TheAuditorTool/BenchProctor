# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest63385(request):
    upload_name = request.FILES['upload'].name
    parts = str(upload_name).split(',')
    data = ','.join(parts)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
