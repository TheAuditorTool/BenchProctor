# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import defusedxml.ElementTree


def BenchmarkTest64466(request):
    raw_body = request.body.decode('utf-8')
    data = '%s' % (raw_body,)
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
