# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest79281(request):
    multipart_value = request.POST.get('multipart_field', '')
    match str(multipart_value):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
        case _: action = 'unknown'
    return JsonResponse({'action': action}, status=200)
