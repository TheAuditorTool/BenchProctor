<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00174Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Origin', '');
        if (!preg_match('#^(asc|desc|name|created)$#', (string)$userInput)) { error_log('enum validation failed'); return response()->json(['error'=>'invalid'], 400); }
        $processed = $userInput;
        $doc = new \DOMDocument();
        @$doc->load('/var/app/data/users.xml');
        $xpath = new \DOMXPath($doc);
        $email = $xpath->evaluate("string(//user[@id='" . $processed . "']/email)");
        return response()->json(['ok' => 1]);
    }
}
