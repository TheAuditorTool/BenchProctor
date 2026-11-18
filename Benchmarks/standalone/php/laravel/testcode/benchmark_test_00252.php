<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00252Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->json('payload', '');
        $transform = fn (string $v): string => trim($v);
        $data = $transform($userInput);
        session(['data' => (string) $data]);
        return response()->json(['ok' => 1]);
    }
}
