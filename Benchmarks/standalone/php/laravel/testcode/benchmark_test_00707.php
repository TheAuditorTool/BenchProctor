<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00707Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->getContent();
        $data = '';
        foreach (explode(',', $userInput) as $token) { $data = $token; }
        session(['data' => (string) $data]);
        return response()->json(['ok' => 1]);
    }
}
