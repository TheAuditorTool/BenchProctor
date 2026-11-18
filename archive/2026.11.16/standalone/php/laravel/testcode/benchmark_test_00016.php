<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Support\Facades\DB;

class BenchmarkTest00016Controller
{
    public function __invoke()
    {
        $userInput = DB::selectOne('SELECT name FROM users LIMIT 1')->name;
        [$data] = [$userInput, 'http'];
        simplexml_load_string($data, 'SimpleXMLElement', LIBXML_NOENT | LIBXML_DTDLOAD);
        return response()->json(['ok' => 1]);
    }
}
