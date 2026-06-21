# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest19428(request):
    xml_value = request.body.decode('utf-8')
    data = ' '.join(str(xml_value).split())
    arr = [10, 20, 30, 40, 50]
    idx = int(str(data))
    return JsonResponse({'lookup': arr[idx]}, status=200)
