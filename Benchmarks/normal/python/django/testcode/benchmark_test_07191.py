# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest07191(request):
    multipart_value = request.POST.get('multipart_field', '')
    parts = str(multipart_value).split(',')
    data = ','.join(parts)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
