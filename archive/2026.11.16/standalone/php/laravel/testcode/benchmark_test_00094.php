<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00094Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->cookie('session_token', '');
        $thunk = function () use ($userInput) { return trim($userInput); };
        $data = $thunk();
        system('gzip -f /var/app/reports/' . (string)$data);
        return response()->json(['ok' => 1]);
    }
}
