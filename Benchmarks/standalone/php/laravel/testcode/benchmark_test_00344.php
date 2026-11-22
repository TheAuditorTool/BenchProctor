<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;

class BenchmarkTest00344Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->getContent();
        $thunk = function () use ($userInput) { return trim($userInput); };
        $data = $thunk();
        $rng = new \Random\Randomizer(new \Random\Engine\Secure());
        $token = bin2hex($rng->getBytes(16));
        DB::statement('UPDATE users SET reset_token = ? WHERE email = ?', [$token, (string)$data]);
        return response()->json(['reset' => 'sent'], 200);
    }
}
