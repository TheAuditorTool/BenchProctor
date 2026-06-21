# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest74388(request):
    upload_name = request.FILES['upload'].name
    data, _sep, _rest = str(upload_name).partition('\x00')
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
