<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00637Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Host', '');
        $data = strtr('{0}', ['{0}' => (string)$userInput]);
        $digest = hash('sha256', (string)$data);
        return response()->json(['ok' => 1]);
    }
}
