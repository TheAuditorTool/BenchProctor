# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import defusedxml.ElementTree


def BenchmarkTest30517(request):
    upload_name = request.FILES['upload'].name
    data = (lambda v: v.strip())(upload_name)
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
