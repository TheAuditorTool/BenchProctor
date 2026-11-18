<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;

class BenchmarkTest00531Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Referer', '');
        $_prefix = strtolower(substr($userInput, 0, 1));
        $data = '';
        switch ($_prefix) {
            case 'h': $data = strtolower($userInput); break;
            case 'f': $data = strtoupper($userInput); break;
            default: $data = trim($userInput); break;
        }
        $result = DB::table('users')->where('id', $data)->first();
        $value = $result->name;
        return response()->json(['ok' => 1]);
    }
}
