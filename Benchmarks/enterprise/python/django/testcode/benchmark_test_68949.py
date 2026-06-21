# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest68949(request):
    upload_name = request.FILES['upload'].name
    data = str(upload_name).replace('\x00', '')
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
