# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest70556(request):
    user_id = request.GET.get('id', '')
    data, _sep, _rest = str(user_id).partition('\x00')
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return JsonResponse({'action': action}, status=200)
