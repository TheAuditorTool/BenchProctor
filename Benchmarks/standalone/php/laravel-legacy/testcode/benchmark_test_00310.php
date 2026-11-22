<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00310Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->getContent();
        $tokens = explode(',', $userInput);
        $data = implode(' ', $tokens);
        \Illuminate\Support\Facades\Session::put(['data' => (string) $data, 'data_updated_at' => time()]);
        return response()->json(['ok' => 1]);
    }
}
