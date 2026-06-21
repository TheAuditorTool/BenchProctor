# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect


def BenchmarkTest49700(request):
    upload_name = request.FILES['upload'].name
    data = ' '.join(str(upload_name).split())
    return redirect(str(data))
