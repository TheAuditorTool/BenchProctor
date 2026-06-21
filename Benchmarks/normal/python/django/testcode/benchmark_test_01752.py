# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import defusedxml.ElementTree


def normalise_input(value):
    return value.strip()

def BenchmarkTest01752(request):
    user_id = request.GET.get('id', '')
    data = normalise_input(user_id)
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
