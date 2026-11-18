<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00662Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->json('payload', '');
        $thunk = function () use ($userInput) { return trim($userInput); };
        $data = $thunk();
        simplexml_load_string($data, 'SimpleXMLElement', LIBXML_NONET);
        return response()->json(['ok' => 1]);
    }
}
