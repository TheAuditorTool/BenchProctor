# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect
import urllib.parse


def BenchmarkTest42212(request):
    upload_name = request.FILES['upload'].name
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(upload_name))
    return redirect(target)
