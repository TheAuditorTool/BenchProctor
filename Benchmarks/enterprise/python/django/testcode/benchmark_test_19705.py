# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest19705(request):
    upload_name = request.FILES['upload'].name
    data = ' '.join(str(upload_name).split())
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
