# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import defusedxml.ElementTree


def to_text(value):
    return str(value).strip()

def BenchmarkTest60122(request):
    upload_name = request.FILES['upload'].name
    data = to_text(upload_name)
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
