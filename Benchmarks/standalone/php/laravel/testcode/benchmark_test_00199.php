<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00199Controller
{
    public function __invoke(Request $request)
    {
        $userInput = ($request->file('upload')?->getClientOriginalName() ?? '');
        $data = '';
        foreach (explode(',', $userInput) as $token) { $data = $token; }
        $digest = hash('sha256', (string)$data);
        return response()->json(['ok' => 1]);
    }
}
