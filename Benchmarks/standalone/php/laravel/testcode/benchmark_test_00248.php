<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00248Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Origin', '');
        $transform = fn (string $v): string => trim($v);
        $data = $transform($userInput);
        $digest = hash('sha256', (string)$data);
        return response()->json(['ok' => 1]);
    }
}
