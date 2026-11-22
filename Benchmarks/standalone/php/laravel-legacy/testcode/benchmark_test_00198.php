<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;

class BenchmarkTest00198Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('X-Custom-Header', '');
        $tokens = explode(',', $userInput);
        $data = implode(' ', $tokens);
        $dbh = DB::getPdo();
        $stmt = $dbh->prepare('SELECT * FROM users WHERE id = ?');
        $stmt->execute([$data]);
        $rows = $stmt->fetchAll(\PDO::FETCH_ASSOC);
        return response()->json(['ok' => 1]);
    }
}
