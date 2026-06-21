# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest79807(request):
    user_id = request.GET.get('id', '')
    data = str(user_id).replace('\x00', '')
    os.seteuid(65534)
    return JsonResponse({"saved": True})
