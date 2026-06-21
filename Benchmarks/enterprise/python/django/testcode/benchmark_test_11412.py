# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest11412(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = '{}'.format(multipart_value)
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return JsonResponse({'action': action}, status=200)
