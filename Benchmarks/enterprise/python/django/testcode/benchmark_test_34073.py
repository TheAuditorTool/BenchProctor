# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect
import urllib.parse


def BenchmarkTest34073(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(referer_value))
    return redirect(target)
