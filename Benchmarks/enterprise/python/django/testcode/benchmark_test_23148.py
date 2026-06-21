# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest23148(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = f'{ua_value:.200s}'
    arr = [10, 20, 30, 40, 50]
    idx = int(str(data))
    return JsonResponse({'lookup': arr[idx]}, status=200)
