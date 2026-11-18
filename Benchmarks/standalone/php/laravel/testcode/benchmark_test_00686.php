<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00686Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->json('payload', '');
        $digest = hash('sha256', (string)$userInput);
        return response()->json(['ok' => 1]);
    }
}
