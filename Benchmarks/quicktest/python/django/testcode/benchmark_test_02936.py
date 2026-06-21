# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import defusedxml.ElementTree


def to_text(value):
    return str(value).strip()

def BenchmarkTest02936(request):
    user_id = request.GET.get('id', '')
    data = to_text(user_id)
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
