# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest02597(request):
    user_id = request.GET.get('id', '')
    data = f'{user_id:.200s}'
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return JsonResponse({'action': action}, status=200)
