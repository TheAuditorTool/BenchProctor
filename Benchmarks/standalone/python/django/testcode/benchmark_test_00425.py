# SPDX-License-Identifier: Apache-2.0
from django.shortcuts import redirect
import json


def BenchmarkTest00425(request):
    json_value = json.loads(request.body or b'{}').get('payload', '')
    return redirect(str(json_value))
