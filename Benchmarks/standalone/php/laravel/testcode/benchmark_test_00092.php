<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00092Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->getContent();
        $data = str_replace("\0", '', $userInput);
        session(['data' => (string) $data]);
        return response()->json(['ok' => 1]);
    }
}
