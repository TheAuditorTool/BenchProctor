<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00388Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Origin', '');
        $words = preg_split('/\s+/', $userInput);
        $data = implode(' ', $words);
        $doc = new \DOMDocument();
        @$doc->load('/var/app/data/users.xml');
        $xpath = new \DOMXPath($doc);
        $nodes = $xpath->query("//user[@id='" . $data . "']");
        return response()->json(['ok' => 1]);
    }
}
