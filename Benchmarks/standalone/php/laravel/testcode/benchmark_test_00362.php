<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00362Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->getContent();
        $data = mb_convert_encoding($userInput, 'UTF-8');
        $doc = new \DOMDocument();
        @$doc->load('/var/app/data/users.xml');
        $xpath = new \DOMXPath($doc);
        $nodes = $xpath->query("//user[@id='" . $data . "']");
        return response()->json(['ok' => 1]);
    }
}
