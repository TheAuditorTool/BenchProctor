# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest08113(request):
    raw_body = request.body.decode('utf-8')
    data, _sep, _rest = str(raw_body).partition('\x00')
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return JsonResponse({'action': action}, status=200)
