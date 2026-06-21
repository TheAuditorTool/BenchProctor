# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest45010(request):
    raw_body = request.body.decode('utf-8')
    data = raw_body if raw_body else 'default'
    arr = [10, 20, 30, 40, 50]
    idx = int(str(data))
    return JsonResponse({'lookup': arr[idx]}, status=200)
