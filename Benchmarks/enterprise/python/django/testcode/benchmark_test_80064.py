# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect
import json


def BenchmarkTest80064(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    return redirect(str(json_value))
