<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00155Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Authorization', '');
        $thunk = function () use ($userInput) { return trim($userInput); };
        $data = $thunk();
        $doc = new \DOMDocument();
        @$doc->load('/var/app/data/users.xml');
        $xpath = new \DOMXPath($doc);
        $nodes = $xpath->query("//user[@id='" . $data . "']");
        return response()->json(['ok' => 1]);
    }
}
