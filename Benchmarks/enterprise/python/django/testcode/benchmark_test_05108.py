# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import defusedxml.ElementTree


def BenchmarkTest05108(request):
    upload_name = request.FILES['upload'].name
    data = ' '.join(str(upload_name).split())
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
