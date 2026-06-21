# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect


def BenchmarkTest42501(request):
    xml_value = request.body.decode('utf-8')
    data = str(xml_value).replace('\x00', '')
    return redirect(str(data))
