# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import defusedxml.ElementTree


def BenchmarkTest51795(request):
    user_id = request.GET.get('id', '')
    defusedxml.ElementTree.fromstring(str(user_id))
    return JsonResponse({"saved": True})
