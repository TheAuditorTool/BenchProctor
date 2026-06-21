# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest47444(request):
    user_id = request.GET.get('id', '')
    if user_id:
        data = user_id
    else:
        data = ''
    arr = [10, 20, 30, 40, 50]
    idx = int(str(data))
    return JsonResponse({'lookup': arr[idx]}, status=200)
