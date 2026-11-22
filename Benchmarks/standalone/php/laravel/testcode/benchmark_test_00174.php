<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00174Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Host', '');
        $_coerced = in_array(strtolower((string)$userInput), ['true', '1', 'yes', 'on'], true) ? 'true' : 'false';
        $parsedBool = $_coerced;
        $doc = new \DOMDocument();
        @$doc->load('/var/app/data/users.xml');
        $xpath = new \DOMXPath($doc);
        $nodes = $xpath->query("//user[@id='" . $parsedBool . "']");
        return response()->json(['ok' => 1]);
    }
}
