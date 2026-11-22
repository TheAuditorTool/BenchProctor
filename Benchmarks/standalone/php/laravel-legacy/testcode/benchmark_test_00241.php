<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00241Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->json('payload', '');
        $data = '';
        foreach (explode(',', $userInput) as $token) { $data = $token; }
        $doc = new \DOMDocument();
        @$doc->load('/var/app/data/users.xml');
        $xpath = new \DOMXPath($doc);
        $email = $xpath->evaluate("string(//user[@id='" . $data . "']/email)");
        return response()->json(['ok' => 1]);
    }
}
