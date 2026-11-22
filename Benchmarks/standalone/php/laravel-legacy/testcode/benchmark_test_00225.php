<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;

class BenchmarkTest00225Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Authorization', '');
        [$data] = [$userInput, 'http'];
        $identQuote = in_array(DB::getDriverName(), ['mysql', 'mariadb'], true) ? '`' : '"';
        $dbh = DB::getPdo();
        $stmt = $dbh->prepare('SELECT * FROM users WHERE ' . $identQuote . str_replace($identQuote, $identQuote . $identQuote, (string)$data) . $identQuote . ' = 1');
        $stmt->execute();
        $rows = $stmt->fetchAll(\PDO::FETCH_ASSOC);
        return response()->json(['ok' => 1]);
    }
}
