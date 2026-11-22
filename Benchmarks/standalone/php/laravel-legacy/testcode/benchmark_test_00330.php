<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Support\Facades\DB;

class BenchmarkTest00330Controller
{
    public function __invoke()
    {
        $userInput = DB::selectOne('SELECT name FROM users LIMIT 1')->name;
        try { $data = json_decode($userInput, true, 512, JSON_THROW_ON_ERROR)['value'] ?? $userInput; }
        catch (\JsonException $e) { $data = $userInput; }
        $doc = new \DOMDocument();
        $doc->loadXML((string)$data, LIBXML_NOENT | LIBXML_DTDLOAD);
        $name = $doc->getElementsByTagName('name')->item(0)?->textContent;
        return response()->json(['ok' => 1]);
    }
}
