# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect
import urllib.parse


def normalise_input(value):
    return value.strip()

def BenchmarkTest62940(request):
    raw_body = request.body.decode('utf-8')
    data = normalise_input(raw_body)
    processed = data[:64]
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(processed))
    return redirect(target)
