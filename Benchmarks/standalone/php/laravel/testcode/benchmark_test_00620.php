<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Support\Facades\DB;

class BenchmarkTest00620Controller
{
    public function __invoke()
    {
        $userInput = DB::selectOne('SELECT text FROM comments LIMIT 1')->text;
        $thunk = function () use ($userInput) { return trim($userInput); };
        $data = $thunk();
        $processed = htmlspecialchars($data, ENT_QUOTES, 'UTF-8');
        return response('<div>' . $processed . '</div>')->header('Content-Type', 'text/html');
    }
}
