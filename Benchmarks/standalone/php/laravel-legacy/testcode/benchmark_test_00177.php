<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;

class BenchmarkTest00177Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->getContent();
        $data = sprintf('%s', $userInput);
        $alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
        $shuffled = str_shuffle(str_repeat($alphabet, 4));
        $token = substr($shuffled, 0, 32);
        DB::statement('UPDATE users SET reset_token = ? WHERE email = ?', [$token, (string)$data]);
        return response()->json(['reset' => 'sent'], 200);
    }
}
