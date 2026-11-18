<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00239Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->cookie('session_token', '');
        $_prefix = strtolower(substr($userInput, 0, 1));
        $data = '';
        switch ($_prefix) {
            case 'h': $data = strtolower($userInput); break;
            case 'f': $data = strtoupper($userInput); break;
            default: $data = trim($userInput); break;
        }
        unserialize($data);
        return response()->json(['ok' => 1]);
    }
}
