# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest42146(request):
    upload_name = request.FILES['upload'].name
    data = '{}'.format(upload_name)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
