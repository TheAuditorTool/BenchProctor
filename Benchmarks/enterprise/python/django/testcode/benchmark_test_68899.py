# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest68899(request):
    user_id = request.GET.get('id', '')
    data = '%s' % str(user_id)
    os.remove(str(data))
    return JsonResponse({"saved": True})
