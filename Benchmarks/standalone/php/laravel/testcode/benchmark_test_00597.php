<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00597Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->json('variables.input', '');
        $data = vsprintf('%1$s', [$userInput]);
        session(['data' => (string) $data]);
        return response()->json(['ok' => 1]);
    }
}
