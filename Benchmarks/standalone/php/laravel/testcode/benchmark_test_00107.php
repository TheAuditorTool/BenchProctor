<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00107Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->getContent();
        $data = sprintf('%s', $userInput);
        $doc = new \DOMDocument();
        $doc->loadXML((string)$data, LIBXML_NOENT | LIBXML_DTDLOAD);
        $name = $doc->getElementsByTagName('name')->item(0)?->textContent;
        return response()->json(['ok' => 1]);
    }
}
