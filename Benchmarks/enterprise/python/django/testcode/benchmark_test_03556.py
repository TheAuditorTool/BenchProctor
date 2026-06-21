# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest03556(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = '%s' % (origin_value,)
    arr = [10, 20, 30, 40, 50]
    idx = int(str(data))
    return JsonResponse({'lookup': arr[idx]}, status=200)
