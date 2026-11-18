<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00606Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Host', '');
        $thunk = function () use ($userInput) { return trim($userInput); };
        $data = $thunk();
        session(['data' => (string) $data]);
        return response()->json(['ok' => 1]);
    }
}
