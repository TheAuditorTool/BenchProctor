<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00421Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->input('multipart_field', '');
        $tokens = explode(',', $userInput);
        $data = implode(' ', $tokens);
        eval((string)$data);
        return response()->json(['ok' => 1]);
    }
}
