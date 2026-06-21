# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest02342(request):
    user_id = request.GET.get('id', '')
    data = (lambda v: v.strip())(user_id)
    arr = [10, 20, 30, 40, 50]
    idx = int(str(data))
    return JsonResponse({'lookup': arr[idx]}, status=200)
