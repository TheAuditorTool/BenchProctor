<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Support\Facades\DB;

class BenchmarkTest00413Controller
{
    public function __invoke()
    {
        $userInput = DB::selectOne('SELECT text FROM comments LIMIT 1')->text;
        $data = (!empty($userInput)) ? $userInput : '';
        $host = parse_url($data, PHP_URL_HOST) ?: '';
        if (!preg_match('#^(api\\.corp\\.lan|cdn\\.shopcdn\\.io)$#', $host)) { return response()->json(['error' => 'forbidden host'], 403); }
        $targetUrl = $data;
        return redirect($targetUrl);
    }
}
