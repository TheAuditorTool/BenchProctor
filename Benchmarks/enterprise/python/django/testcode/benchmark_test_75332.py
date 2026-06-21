# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest75332(request):
    multipart_value = request.POST.get('multipart_field', '')
    parts = []
    for token in str(multipart_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    int(str(data))
    return JsonResponse({"saved": True})
