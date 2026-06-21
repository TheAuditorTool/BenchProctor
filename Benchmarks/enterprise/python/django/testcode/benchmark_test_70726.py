# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest70726(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = str(host_value).replace('\x00', '')
    arr = [10, 20, 30, 40, 50]
    idx = int(str(data))
    return JsonResponse({'lookup': arr[idx]}, status=200)
