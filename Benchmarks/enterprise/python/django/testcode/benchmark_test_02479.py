# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect
import urllib.parse


def BenchmarkTest02479(request):
    user_id = request.GET.get('id', '')
    data = (lambda v: v.strip())(user_id)
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
