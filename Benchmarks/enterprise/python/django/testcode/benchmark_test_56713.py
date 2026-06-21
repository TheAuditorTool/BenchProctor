# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import defusedxml.ElementTree


def BenchmarkTest56713(request):
    upload_name = request.FILES['upload'].name
    data = '%s' % str(upload_name)
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
