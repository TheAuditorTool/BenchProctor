# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import unquote
import defusedxml.ElementTree


def BenchmarkTest51105(request):
    user_id = request.GET.get('id', '')
    data = unquote(user_id)
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
