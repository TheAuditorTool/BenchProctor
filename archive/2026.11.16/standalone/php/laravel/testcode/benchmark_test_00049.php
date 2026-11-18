<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00049Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->input('multipart_field', '');
        $thunk = function () use ($userInput) { return trim($userInput); };
        $data = $thunk();
        simplexml_load_string($data, 'SimpleXMLElement', LIBXML_NONET);
        return response()->json(['ok' => 1]);
    }
}
