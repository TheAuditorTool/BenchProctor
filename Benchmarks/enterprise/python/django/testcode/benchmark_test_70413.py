# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest70413(request):
    user_id = request.GET.get('id', '')
    data = user_id if user_id else 'default'
    values = str(data).split(',')
    if values:
        return JsonResponse({'first': values[0], 'dropped': len(values) - 1}, status=200)
    return JsonResponse({"saved": True})
