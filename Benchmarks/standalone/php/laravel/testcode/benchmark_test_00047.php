<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Support\Facades\DB;

class BenchmarkTest00047Controller
{
    public function __invoke()
    {
        $userInput = DB::selectOne('SELECT bio FROM profiles LIMIT 1')->bio;
        if (!preg_match('#^[a-zA-Z0-9 _.\\#~\\-]+$#', $userInput)) { error_log('input validation failed'); return response()->json(['error'=>'invalid'], 400); }
        $processed = $userInput;
        $content = file_get_contents('/var/app/data/' . (string)$processed);
        return response()->json(['ok' => 1]);
    }
}
