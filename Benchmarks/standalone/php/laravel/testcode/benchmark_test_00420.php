<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00420Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->input('field', '');
        $asText = function ($v): string { return trim((string) $v); };
        $data = $asText($userInput);
        $digest = md5((string)$data);
        return response()->json(['ok' => 1]);
    }
}
