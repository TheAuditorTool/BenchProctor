# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect


def BenchmarkTest28673(request):
    user_id = request.GET.get('id', '')
    data = f'{user_id:.200s}'
    return redirect(str(data))
