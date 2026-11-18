<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Support\Facades\DB;

class BenchmarkTest00346Controller
{
    public function __invoke()
    {
        $userInput = DB::selectOne('SELECT bio FROM profiles LIMIT 1')->bio;
        $words = preg_split('/\s+/', $userInput);
        $data = implode(' ', $words);
        file_put_contents('/var/uploads/' . $data, 'data');
        return response()->json(['ok' => 1]);
    }
}
