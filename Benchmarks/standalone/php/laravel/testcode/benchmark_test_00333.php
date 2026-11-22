<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Support\Facades\DB;

class BenchmarkTest00333Controller
{
    public function __invoke()
    {
        $userInput = file_get_contents('/tmp/data');
        $data = hex2bin($userInput);
        $_coerced = (int)$data;
        $parsedId = $_coerced;
        $dbh = DB::getPdo();
        $stmt = $dbh->prepare('SELECT * FROM users WHERE id = \'' . $parsedId . '\'');
        $stmt->execute();
        $rows = $stmt->fetchAll(\PDO::FETCH_ASSOC);
        return response()->json(['ok' => 1]);
    }
}
