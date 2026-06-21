# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect


def BenchmarkTest50793(request):
    user_id = request.GET.get('id', '')
    data = '%s' % (user_id,)
    return redirect(str(data))
