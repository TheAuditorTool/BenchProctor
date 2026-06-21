# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest02543(request):
    user_id = request.GET.get('id', '')
    data = '%s' % (user_id,)
    os.chmod('/var/app/data/' + str(data), 0o777)
    return JsonResponse({"saved": True})
