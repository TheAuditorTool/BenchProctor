<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00009Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Referer', '');
        $data = '';
        foreach (explode(',', $userInput) as $token) { $data = $token; }
        $digest = hash('sha256', (string)$data);
        return response()->json(['ok' => 1]);
    }
}
