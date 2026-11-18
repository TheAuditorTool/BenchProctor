<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;

class BenchmarkTest00485Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('X-Custom-Header', '');
        $data = str_replace("\0", '', $userInput);
        DB::select('SELECT * FROM users WHERE id = ?', [$data]);
        return response()->json(['ok' => 1]);
    }
}
