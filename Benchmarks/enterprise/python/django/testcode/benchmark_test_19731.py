# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest19731(request):
    upload_name = request.FILES['upload'].name
    data = (lambda v: v.strip())(upload_name)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
