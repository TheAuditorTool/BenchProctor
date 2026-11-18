<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00221Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->json('payload', '');
        $data = strtr('{0}', ['{0}' => (string)$userInput]);
        $digest = hash('sha256', (string)$data);
        return response()->json(['ok' => 1]);
    }
}
