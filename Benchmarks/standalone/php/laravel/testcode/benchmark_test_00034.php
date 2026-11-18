<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00034Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->getContent();
        [$data] = [$userInput, 'http'];
        session(['data' => (string) $data]);
        return response()->json(['ok' => 1]);
    }
}
