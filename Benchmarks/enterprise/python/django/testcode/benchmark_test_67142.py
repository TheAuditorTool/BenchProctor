# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest67142(request):
    xml_value = request.body.decode('utf-8')
    if xml_value:
        data = xml_value
    else:
        data = ''
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return JsonResponse({'action': action}, status=200)
