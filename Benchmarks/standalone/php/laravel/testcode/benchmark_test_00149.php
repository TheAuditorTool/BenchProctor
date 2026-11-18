<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Support\Facades\DB;

class BenchmarkTest00149Controller
{
    public function __invoke()
    {
        $userInput = DB::selectOne('SELECT name FROM users LIMIT 1')->name;
        $data = "{$userInput}";
        $processed = htmlspecialchars($data, ENT_QUOTES, 'UTF-8');
        return response('<div>' . $processed . '</div>')->header('Content-Type', 'text/html');
    }
}
