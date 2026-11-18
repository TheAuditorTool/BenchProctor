<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00560Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->json('payload', '');
        $data = '';
        foreach (explode(',', $userInput) as $token) { $data = $token; }
        simplexml_load_string($data, 'SimpleXMLElement', LIBXML_NONET);
        return response()->json(['ok' => 1]);
    }
}
