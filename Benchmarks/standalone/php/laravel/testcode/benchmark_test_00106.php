<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00106Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->getContent();
        $data = '';
        foreach (explode(',', $userInput) as $token) { $data = $token; }
        $errno = 0; $errstr = '';
        fsockopen((string)$data, 80, $errno, $errstr, 30);
        return response()->json(['ok' => 1]);
    }
}
