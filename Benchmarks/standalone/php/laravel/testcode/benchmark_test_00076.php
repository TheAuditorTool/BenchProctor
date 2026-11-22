<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00076Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->json('payload', '');
        $data = vsprintf('%1$s', [$userInput]);
        $digest = md5((string)$data);
        return response()->json(['ok' => 1]);
    }
}
