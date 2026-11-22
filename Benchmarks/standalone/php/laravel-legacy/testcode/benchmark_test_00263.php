<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Support\Facades\DB;

class BenchmarkTest00263Controller
{
    public function __invoke()
    {
        $userInput = DB::selectOne('SELECT name FROM users LIMIT 1')->name;
        $thunk = function () use ($userInput) { return trim($userInput); };
        $data = $thunk();
        $doc = new \DOMDocument();
        $doc->loadXML((string)$data, LIBXML_NONET);
        $name = $doc->getElementsByTagName('name')->item(0)?->textContent;
        return response()->json(['ok' => 1]);
    }
}
