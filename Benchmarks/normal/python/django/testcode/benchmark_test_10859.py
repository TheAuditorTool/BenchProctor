# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import defusedxml.ElementTree


def BenchmarkTest10859(request):
    upload_name = request.FILES['upload'].name
    data = '%s' % (upload_name,)
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
