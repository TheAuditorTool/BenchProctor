# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import unquote


def BenchmarkTest68232(request):
    user_id = request.GET.get('id', '')
    data = unquote(user_id)
    exec(str(data))
    return JsonResponse({"saved": True})
