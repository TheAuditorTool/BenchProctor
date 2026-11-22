<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;

class BenchmarkTest00022Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('User-Agent', '');
        $transform = fn (string $v): string => trim($v);
        $data = $transform($userInput);
        $_coerced = (int)$data;
        $parsedId = $_coerced;
        $dbh = DB::getPdo();
        $stmt = $dbh->prepare('SELECT * FROM users WHERE id = \'' . $parsedId . '\'');
        $stmt->execute();
        $rows = $stmt->fetchAll(\PDO::FETCH_ASSOC);
        return response()->json(['ok' => 1]);
    }
}
