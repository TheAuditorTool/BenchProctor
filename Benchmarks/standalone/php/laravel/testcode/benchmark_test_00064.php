<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00064Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->input('multipart_field', '');
        $data = sprintf('%s', $userInput);
        $doc = new \DOMDocument();
        $doc->loadXML((string)$data, LIBXML_NONET);
        $name = $doc->getElementsByTagName('name')->item(0)?->textContent;
        return response()->json(['ok' => 1]);
    }
}
