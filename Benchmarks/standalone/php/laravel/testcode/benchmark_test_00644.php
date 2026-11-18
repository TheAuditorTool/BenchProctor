<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00644Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->getContent();
        $data = base64_decode($userInput);
        $digest = hash('sha256', (string)$data);
        return response()->json(['ok' => 1]);
    }
}
