<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00162Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('X-Custom-Header', '');
        $data = '';
        foreach (explode(',', $userInput) as $token) { $data = $token; }
        json_decode($data, true);
        return response()->json(['ok' => 1]);
    }
}
