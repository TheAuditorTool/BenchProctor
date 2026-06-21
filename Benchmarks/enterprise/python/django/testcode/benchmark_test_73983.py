# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest73983(request):
    user_id = request.GET.get('id', '')
    data = '{}'.format(user_id)
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
        case _: action = 'unknown'
    return JsonResponse({'action': action}, status=200)
