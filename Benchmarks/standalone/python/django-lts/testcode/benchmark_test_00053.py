# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import unquote


def BenchmarkTest00053(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = unquote(referer_value)
    exec(str(data))
    return JsonResponse({"saved": True})
