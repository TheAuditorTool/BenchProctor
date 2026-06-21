# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import defusedxml.ElementTree


def BenchmarkTest29681(request):
    upload_name = request.FILES['upload'].name
    data = upload_name if upload_name else 'default'
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
