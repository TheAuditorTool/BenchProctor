<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00213Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->json('payload', '');
        try { $data = json_decode($userInput, true, 512, JSON_THROW_ON_ERROR)['value'] ?? $userInput; }
        catch (\JsonException $e) { $data = $userInput; }
        if (!preg_match('#^[a-zA-Z0-9 _.%~\\-]+$#', $data)) { error_log('input validation failed'); return response()->json(['error'=>'invalid'], 400); }
        $processed = $data;
        $doc = new \DOMDocument();
        @$doc->load('/var/app/data/users.xml');
        $xpath = new \DOMXPath($doc);
        $nodes = $xpath->query("//user[@id='" . $processed . "']");
        return response()->json(['ok' => 1]);
    }
}
