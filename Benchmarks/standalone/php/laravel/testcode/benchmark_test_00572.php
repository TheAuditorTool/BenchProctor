<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00572Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->cookie('session_token', '');
        $data = strtr('{0}', ['{0}' => (string)$userInput]);
        $digest = md5((string)$data);
        return response()->json(['ok' => 1]);
    }
}
