# SPDX-License-Identifier: Apache-2.0
from django.shortcuts import redirect


def BenchmarkTest00270(request):
    upload_name = request.FILES['upload'].name
    data = f'{upload_name!s}'
    return redirect(str(data))
