# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest31458(request):
    upload_name = request.FILES['upload'].name
    def normalize(value):
        return value.strip()
    data = normalize(upload_name)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
