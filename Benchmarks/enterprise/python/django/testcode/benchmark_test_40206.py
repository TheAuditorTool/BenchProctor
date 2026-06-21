# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest40206(request):
    user_id = request.GET.get('id', '')
    os.chmod('/var/app/data/' + str(user_id), 0o777)
    return JsonResponse({"saved": True})
