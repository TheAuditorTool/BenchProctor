# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest17262(request):
    raw_body = request.body.decode('utf-8')
    if raw_body:
        data = raw_body
    else:
        data = ''
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
        case _: action = 'unknown'
    return JsonResponse({'action': action}, status=200)
