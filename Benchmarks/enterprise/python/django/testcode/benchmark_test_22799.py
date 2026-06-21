# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest22799(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = f'{multipart_value}'
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
