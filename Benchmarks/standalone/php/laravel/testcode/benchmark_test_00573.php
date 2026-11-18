<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Support\Facades\DB;

class BenchmarkTest00573Controller
{
    public function __invoke()
    {
        $userInput = DB::selectOne('SELECT name FROM users LIMIT 1')->name;
        $form = new class($userInput) { public function __construct(public readonly string $payload) {} };
        $data = $form->payload;
        $digest = md5((string)$data);
        return response()->json(['ok' => 1]);
    }
}
