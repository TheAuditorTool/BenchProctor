# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect


def BenchmarkTest24804(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = f'{host_value:.200s}'
    return redirect(str(data))
