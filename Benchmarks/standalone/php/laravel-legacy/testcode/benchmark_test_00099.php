<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00099Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->input('multipart_field', '');
        $data = urldecode($userInput);
        \Illuminate\Support\Facades\Cache::forever('tenant:display_name', (string) $data);
        return response()->json(['ok' => 1]);
    }
}
