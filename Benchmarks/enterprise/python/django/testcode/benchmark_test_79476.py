# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest79476(request):
    user_id = request.GET.get('id', '')
    data = user_id if user_id else 'default'
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
        case _: action = 'unknown'
    return JsonResponse({'action': action}, status=200)
