# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest58508(request):
    upload_name = request.FILES['upload'].name
    match str(upload_name):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return JsonResponse({'action': action}, status=200)
