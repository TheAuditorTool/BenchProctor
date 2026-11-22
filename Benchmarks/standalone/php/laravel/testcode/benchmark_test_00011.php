<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00011Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->json('variables.input', '');
        $transform = fn (string $v): string => trim($v);
        $data = $transform($userInput);
        $digest = md5((string)$data);
        return response()->json(['ok' => 1]);
    }
}
