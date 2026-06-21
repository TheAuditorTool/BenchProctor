# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import defusedxml.ElementTree


def BenchmarkTest67787(request):
    upload_name = request.FILES['upload'].name
    data = str(upload_name).replace('\x00', '')
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
