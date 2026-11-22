<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00139Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Authorization', '');
        [$data] = [$userInput, 'http'];
        $digest = hash('sha256', (string)$data);
        return response()->json(['ok' => 1]);
    }
}
