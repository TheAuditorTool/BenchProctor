<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00006Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Origin', '');
        $thunk = function () use ($userInput) { return trim($userInput); };
        $data = $thunk();
        $digest = md5((string)$data);
        return response()->json(['ok' => 1]);
    }
}
