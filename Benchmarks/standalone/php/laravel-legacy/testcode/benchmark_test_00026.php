<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Support\Facades\DB;

class BenchmarkTest00026Controller
{
    public function __invoke()
    {
        $userInput = DB::selectOne('SELECT body FROM mq_messages ORDER BY id DESC LIMIT 1')->body;
        $data = (!empty($userInput)) ? $userInput : '';
        $identQuote = in_array(DB::getDriverName(), ['mysql', 'mariadb'], true) ? '`' : '"';
        $rows = DB::table('users')->whereRaw($identQuote . str_replace($identQuote, $identQuote . $identQuote, (string)$data) . $identQuote . ' = 1')->get();
        return response()->json(['ok' => 1]);
    }
}
