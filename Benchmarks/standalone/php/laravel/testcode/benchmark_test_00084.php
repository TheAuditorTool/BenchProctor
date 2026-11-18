<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Validator;

class BenchmarkTest00084Controller
{
    public function __invoke()
    {
        $userInput = DB::selectOne('SELECT text FROM comments LIMIT 1')->text;
        $data = "{$userInput}";
        $_valid = Validator::make(['value' => (string)$data], ['value' => ['regex:' . '#^[a-zA-Z0-9 _.%~\\-]+$#']]);
        if ($_valid->fails()) { error_log('schema validation failed'); return response()->json(['error'=>'invalid'], 400); }
        $processed = (string)$data;
        $doc = new \DOMDocument();
        @$doc->load('/var/app/data/users.xml');
        $xpath = new \DOMXPath($doc);
        $nodes = $xpath->query("//user[@id='" . $processed . "']");
        return response()->json(['ok' => 1]);
    }
}
