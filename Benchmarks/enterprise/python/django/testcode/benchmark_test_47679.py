# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import defusedxml.ElementTree


def BenchmarkTest47679(request):
    user_id = request.GET.get('id', '')
    prefix = ''
    data = prefix + str(user_id)
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
