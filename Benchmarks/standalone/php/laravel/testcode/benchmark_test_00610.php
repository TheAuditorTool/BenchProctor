<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00610Controller
{
    public function __invoke(Request $request)
    {
        $userInput = ($request->route('id') ?? $request->input('id', ''));
        $tokens = explode(',', $userInput);
        $data = implode(' ', $tokens);
        $digest = hash('sha256', (string)$data);
        return response()->json(['ok' => 1]);
    }
}
