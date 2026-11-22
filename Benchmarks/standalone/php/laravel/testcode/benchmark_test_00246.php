<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Support\Facades\DB;

class BenchmarkTest00246Controller
{
    public function __invoke()
    {
        $userInput = DB::selectOne('SELECT text FROM comments LIMIT 1')->text;
        $data = '';
        foreach (explode(',', $userInput) as $token) { $data = $token; }
        return response('', 302)->header('Location', (string)$data);
    }
}
