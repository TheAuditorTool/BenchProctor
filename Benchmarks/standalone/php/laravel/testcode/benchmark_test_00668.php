<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00668Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->input('field', '');
        $data = (!empty($userInput)) ? $userInput : '';
        simplexml_load_string($data, 'SimpleXMLElement', LIBXML_NONET);
        return response()->json(['ok' => 1]);
    }
}
