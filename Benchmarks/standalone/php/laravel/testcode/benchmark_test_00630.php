<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00630Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Origin', '');
        $asText = function ($v): string { return trim((string) $v); };
        $data = $asText($userInput);
        unserialize($data);
        return response()->json(['ok' => 1]);
    }
}
