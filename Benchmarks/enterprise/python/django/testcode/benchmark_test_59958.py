# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect
import urllib.parse


def BenchmarkTest59958(request):
    upload_name = request.FILES['upload'].name
    data, _sep, _rest = str(upload_name).partition('\x00')
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
