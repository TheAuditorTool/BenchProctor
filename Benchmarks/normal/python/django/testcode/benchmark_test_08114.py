# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect


def BenchmarkTest08114(request):
    user_id = request.GET.get('id', '')
    return redirect(str(user_id))
