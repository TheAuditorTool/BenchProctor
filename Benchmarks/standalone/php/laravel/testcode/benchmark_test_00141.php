<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00141Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Authorization', '');
        $transform = fn (string $v): string => trim($v);
        $data = $transform($userInput);
        $_coerced = (float)$data;
        $processed = $_coerced;
        eval((string)$processed);
        return response()->json(['ok' => 1]);
    }
}
