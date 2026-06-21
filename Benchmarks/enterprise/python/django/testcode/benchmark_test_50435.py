# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest50435(request):
    raw_body = request.body.decode('utf-8')
    data = ' '.join(str(raw_body).split())
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return JsonResponse({'action': action}, status=200)
