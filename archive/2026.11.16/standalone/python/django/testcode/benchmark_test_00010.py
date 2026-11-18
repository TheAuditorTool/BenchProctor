# SPDX-License-Identifier: Apache-2.0
from django.shortcuts import redirect


def BenchmarkTest00010(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = str(header_value).replace('\x00', '')
    return redirect(str(data))
