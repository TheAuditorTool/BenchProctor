# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest67416(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = f'{multipart_value:.200s}'
    result = 100 / int(str(data))
    return JsonResponse({"saved": True})
