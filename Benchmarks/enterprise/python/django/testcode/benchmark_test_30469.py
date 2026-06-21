# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect


def BenchmarkTest30469(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = '%s' % str(host_value)
    return redirect(str(data))
