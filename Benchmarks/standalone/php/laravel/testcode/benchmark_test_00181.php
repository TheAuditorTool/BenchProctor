<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Support\Facades\DB;

class BenchmarkTest00181Controller
{
    public function __invoke()
    {
        $userInput = DB::selectOne('SELECT name FROM users LIMIT 1')->name;
        $tokens = explode(',', $userInput);
        $data = implode(' ', $tokens);
        $scheme = strtolower((string) parse_url($data, PHP_URL_SCHEME));
        $host = parse_url($data, PHP_URL_HOST) ?: '';
        if (!in_array($scheme, ['http', 'https'], true) || preg_match('/[\x00-\x20\\\\]/', (string) $data) || !preg_match('#^(api\\.corp\\.lan|cdn\\.shopcdn\\.io)$#', $host)) { return response()->json(['error' => 'forbidden host'], 403); }
        $targetUrl = $data;
        return redirect($targetUrl);
    }
}
