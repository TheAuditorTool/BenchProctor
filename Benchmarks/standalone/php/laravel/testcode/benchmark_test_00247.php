<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Support\Facades\DB;

class BenchmarkTest00247Controller
{
    public function __invoke()
    {
        $userInput = DB::selectOne('SELECT text FROM comments LIMIT 1')->text;
        $data = str_replace("\0", '', $userInput);
        $records = (int) $data;
        $frame = str_repeat("\0", (int) ($records * 16));
        return response()->json(['frame_bytes' => strlen($frame)], 200);
    }
}
