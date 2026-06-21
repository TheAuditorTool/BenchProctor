# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest30440(request):
    upload_name = request.FILES['upload'].name
    prefix = ''
    data = prefix + str(upload_name)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
