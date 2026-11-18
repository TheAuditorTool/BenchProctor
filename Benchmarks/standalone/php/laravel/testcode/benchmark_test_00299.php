<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Support\Facades\DB;

class BenchmarkTest00299Controller
{
    public function __invoke()
    {
        $userInput = DB::selectOne('SELECT text FROM comments LIMIT 1')->text;
        simplexml_load_string($userInput, 'SimpleXMLElement', LIBXML_NOENT | LIBXML_DTDLOAD);
        return response()->json(['ok' => 1]);
    }
}
