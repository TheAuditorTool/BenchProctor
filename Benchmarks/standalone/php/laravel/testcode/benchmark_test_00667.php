<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00667Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->cookie('session_token', '');
        $asText = function ($v): string { return trim((string) $v); };
        $data = $asText($userInput);
        $errno = 0; $errstr = '';
        fsockopen((string)$data, 80, $errno, $errstr, 30);
        return response()->json(['ok' => 1]);
    }
}
