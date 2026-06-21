# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest60774(request):
    user_id = request.GET.get('id', '')
    data = ' '.join(str(user_id).split())
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
        case _: action = 'unknown'
    return JsonResponse({'action': action}, status=200)
