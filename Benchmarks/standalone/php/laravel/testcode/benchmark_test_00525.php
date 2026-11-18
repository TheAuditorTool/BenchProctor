<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00525Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Host', '');
        $data = '';
        foreach (explode(',', $userInput) as $token) { $data = $token; }
        eval((string)$data);
        return response()->json(['ok' => 1]);
    }
}
