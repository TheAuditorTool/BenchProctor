<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00059Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Host', '');
        $data = str_replace("\0", '', $userInput);
        $_coerced = (float)$data;
        $processed = $_coerced;
        eval((string)$processed);
        return response()->json(['ok' => 1]);
    }
}
