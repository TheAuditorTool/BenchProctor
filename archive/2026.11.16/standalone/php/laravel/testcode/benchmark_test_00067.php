<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00067Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('X-Forwarded-For', '');
        $form = new class($userInput) { public function __construct(public readonly string $payload) {} };
        $data = $form->payload;
        $_coerced = in_array(strtolower((string)$data), ['true', '1', 'yes', 'on'], true) ? 'true' : 'false';
        $parsedBool = $_coerced;
        $doc = new \DOMDocument();
        @$doc->load('/var/app/data/users.xml');
        $xpath = new \DOMXPath($doc);
        $nodes = $xpath->query("//user[@id='" . $parsedBool . "']");
        return response()->json(['ok' => 1]);
    }
}
