<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;

class BenchmarkTest00273Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Referer', '');
        $words = preg_split('/\s+/', $userInput);
        $data = implode(' ', $words);
        $dbh = DB::getPdo();
        $stmt = $dbh->prepare('SELECT * FROM users WHERE id = \'' . $data . '\'');
        $stmt->execute();
        $rows = $stmt->fetchAll(\PDO::FETCH_ASSOC);
        return response()->json(['ok' => 1]);
    }
}
