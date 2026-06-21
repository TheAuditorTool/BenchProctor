# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
import defusedxml.ElementTree


@dataclass
class FormData:
    payload: str

def BenchmarkTest24304(request):
    upload_name = request.FILES['upload'].name
    data = FormData(payload=upload_name).payload
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
