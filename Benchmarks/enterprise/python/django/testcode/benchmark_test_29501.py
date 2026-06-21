# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest29501(request):
    upload_name = request.FILES['upload'].name
    data = f'{upload_name:.200s}'
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
