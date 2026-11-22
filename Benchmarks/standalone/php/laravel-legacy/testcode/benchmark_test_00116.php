<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Support\Facades\DB;

class BenchmarkTest00116Controller
{
    public function __invoke()
    {
        $userInput = DB::selectOne('SELECT bio FROM profiles LIMIT 1')->bio;
        if (!preg_match('#^(asc|desc|name|created)$#', (string)$userInput)) { error_log('enum validation failed'); return response()->json(['error'=>'invalid'], 400); }
        $processed = $userInput;
        $dbh = DB::getPdo();
        $stmt = $dbh->prepare('SELECT * FROM users ORDER BY ' . $processed);
        $stmt->execute();
        $rows = $stmt->fetchAll(\PDO::FETCH_ASSOC);
        return response()->json(['ok' => 1]);
    }
}
