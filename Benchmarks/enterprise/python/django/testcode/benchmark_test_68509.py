# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import defusedxml.ElementTree


def BenchmarkTest68509(request):
    upload_name = request.FILES['upload'].name
    defusedxml.ElementTree.fromstring(str(upload_name))
    return JsonResponse({"saved": True})
