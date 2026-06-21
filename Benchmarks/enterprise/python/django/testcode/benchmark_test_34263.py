# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest34263(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = str(multipart_value).replace('\x00', '')
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
