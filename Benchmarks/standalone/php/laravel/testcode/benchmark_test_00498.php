<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Support\Facades\DB;

class BenchmarkTest00498Controller
{
    public function __invoke()
    {
        $userInput = DB::selectOne('SELECT name FROM users LIMIT 1')->name;
        $data = base64_decode($userInput);
        $processed = (new \HTMLPurifier())->purify($data);
        return response('<div>' . $processed . '</div>')->header('Content-Type', 'text/html');
    }
}
