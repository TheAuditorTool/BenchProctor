<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00280Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->getContent();
        $data = strtr('{0}', ['{0}' => (string)$userInput]);
        json_decode($data, true);
        return response()->json(['ok' => 1]);
    }
}
