<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Support\Facades\DB;

class BenchmarkTest00221Controller
{
    public function __invoke()
    {
        $userInput = config('app.value', '');
        $transform = fn (string $v): string => trim($v);
        $data = $transform($userInput);
        $dbh = DB::getPdo();
        $stmt = $dbh->prepare('SELECT * FROM users WHERE id = \'' . $data . '\'');
        $stmt->execute();
        $rows = $stmt->fetchAll(\PDO::FETCH_ASSOC);
        return response()->json(['ok' => 1]);
    }
}
