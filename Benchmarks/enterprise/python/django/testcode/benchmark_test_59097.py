# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect
import urllib.parse


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest59097(request):
    user_id = request.GET.get('id', '')
    reader = make_reader(user_id)
    data = reader()
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
