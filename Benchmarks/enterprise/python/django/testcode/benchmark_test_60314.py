# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest60314(request):
    user_id = request.GET.get('id', '')
    prefix = ''
    data = prefix + str(user_id)
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return JsonResponse({'action': action}, status=200)
