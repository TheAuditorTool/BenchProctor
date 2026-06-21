# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest19381(request):
    user_id = request.GET.get('id', '')
    data = (lambda v: v.strip())(user_id)
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
        case _: action = 'unknown'
    return JsonResponse({'action': action}, status=200)
