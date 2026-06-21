# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest06451(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = f'{multipart_value:.200s}'
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
