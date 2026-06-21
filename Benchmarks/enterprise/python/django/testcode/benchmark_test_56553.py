# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest56553(request):
    user_id = request.GET.get('id', '')
    data = '%s' % str(user_id)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return JsonResponse({"saved": True})
