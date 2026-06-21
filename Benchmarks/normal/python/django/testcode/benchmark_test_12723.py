# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest12723(request):
    user_id = request.GET.get('id', '')
    prefix = ''
    data = prefix + str(user_id)
    values = str(data).split(',')
    if values:
        return JsonResponse({'first': values[0], 'dropped': len(values) - 1}, status=200)
    return JsonResponse({"saved": True})
