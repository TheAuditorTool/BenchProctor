# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest38728(request):
    user_id = request.GET.get('id', '')
    data = '%s' % str(user_id)
    request.session['user'] = str(data)
    return JsonResponse({"saved": True})
