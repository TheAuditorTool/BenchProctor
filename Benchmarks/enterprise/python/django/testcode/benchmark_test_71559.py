# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest71559(request):
    xml_value = request.body.decode('utf-8')
    parts = []
    for token in str(xml_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    arr = [10, 20, 30, 40, 50]
    idx = int(str(data))
    return JsonResponse({'lookup': arr[idx]}, status=200)
