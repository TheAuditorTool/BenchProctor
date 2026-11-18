<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Support\Facades\DB;

class BenchmarkTest00098Controller
{
    public function __invoke()
    {
        $userInput = DB::selectOne('SELECT name FROM users LIMIT 1')->name;
        $data = json_decode($userInput, true)['value'] ?? '';
        simplexml_load_string($data, 'SimpleXMLElement', LIBXML_NONET);
        return response()->json(['ok' => 1]);
    }
}
