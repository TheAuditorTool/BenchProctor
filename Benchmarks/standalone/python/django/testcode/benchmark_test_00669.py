# SPDX-License-Identifier: Apache-2.0
from django.shortcuts import redirect


def BenchmarkTest00669(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = host_value if host_value else 'default'
    return redirect(str(data))
