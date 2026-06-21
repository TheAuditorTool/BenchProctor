# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest49366(request):
    user_id = request.GET.get('id', '')
    data = '%s' % str(user_id)
    values = str(data).split(',')
    if values:
        return JsonResponse({'first': values[0], 'dropped': len(values) - 1}, status=200)
    return JsonResponse({"saved": True})
