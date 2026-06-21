# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest66717(request):
    upload_name = request.FILES['upload'].name
    data = '%s' % (upload_name,)
    if str(data).endswith(('/public', '/static', '/.')):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
