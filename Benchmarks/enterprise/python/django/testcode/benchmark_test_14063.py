# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest14063(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = f'{header_value:.200s}'
    eval(str(data))
    return JsonResponse({"saved": True})
