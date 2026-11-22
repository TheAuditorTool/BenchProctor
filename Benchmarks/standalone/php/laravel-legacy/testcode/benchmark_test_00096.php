<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;

class BenchmarkTest00096Controller
{
    public function __invoke(Request $request)
    {
        $userInput = ($request->file('upload')?->getClientOriginalName() ?? '');
        $data = vsprintf('%1$s', [$userInput]);
        $alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
        $token = '';
        for ($i = 0; $i < 32; $i++) {
            $token .= $alphabet[random_int(0, strlen($alphabet) - 1)];
        }
        DB::statement('UPDATE users SET reset_token = ? WHERE email = ?', [$token, (string)$data]);
        return response()->json(['reset' => 'sent'], 200);
    }
}
