# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect


def BenchmarkTest33235(request):
    user_id = request.GET.get('id', '')
    data = user_id if user_id else 'default'
    return redirect(str(data))
