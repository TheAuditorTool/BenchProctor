<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;

class BenchmarkTest00105Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->cookie('session_token', '');
        $data = base64_decode($userInput);
        $dbh = DB::getPdo();
        $stmt = $dbh->prepare('SELECT * FROM users WHERE id = \'' . $data . '\'');
        $stmt->execute();
        $rows = $stmt->fetchAll(\PDO::FETCH_ASSOC);
        return response()->json(['ok' => 1]);
    }
}
