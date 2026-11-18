<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00205Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('X-Forwarded-For', '');
        $transform = fn (string $v): string => trim($v);
        $data = $transform($userInput);
        json_decode($data, true);
        return response()->json(['ok' => 1]);
    }
}
