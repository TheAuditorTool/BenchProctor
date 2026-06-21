# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest40376(request):
    upload_name = request.FILES['upload'].name
    data = '%s' % str(upload_name)
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return JsonResponse({'action': action}, status=200)
