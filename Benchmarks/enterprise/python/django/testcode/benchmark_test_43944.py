# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect


def BenchmarkTest43944(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    return redirect(str(header_value))
