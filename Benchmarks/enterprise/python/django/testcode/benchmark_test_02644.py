# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest02644(request):
    upload_name = request.FILES['upload'].name
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(upload_name))
    return resp
