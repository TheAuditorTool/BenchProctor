# SPDX-License-Identifier: Apache-2.0
from django.shortcuts import redirect


def BenchmarkTest00517(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = str(referer_value).replace('\x00', '')
    return redirect(str(data))
