# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import defusedxml.ElementTree


def ensure_str(value):
    return str(value)

def BenchmarkTest09627(request):
    user_id = request.GET.get('id', '')
    data = ensure_str(user_id)
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
