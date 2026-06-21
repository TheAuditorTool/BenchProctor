# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest57052(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = multipart_value if multipart_value else 'default'
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return JsonResponse({'action': action}, status=200)
