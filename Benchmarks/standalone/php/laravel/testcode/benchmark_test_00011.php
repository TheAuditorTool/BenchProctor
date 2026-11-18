<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00011Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->json('payload', '');
        $doc = new \DOMDocument();
        @$doc->load('/var/app/data/users.xml');
        $xpath = new \DOMXPath($doc);
        $nodes = $xpath->query("//user[@id='" . $userInput . "']");
        return response()->json(['ok' => 1]);
    }
}
