# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest30627(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = referer_value if referer_value else 'default'
    os.chmod('/var/app/data/' + str(data), 0o777)
    return JsonResponse({"saved": True})
