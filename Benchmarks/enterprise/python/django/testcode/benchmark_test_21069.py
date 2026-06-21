# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect


def BenchmarkTest21069(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    return redirect(str(auth_header))
