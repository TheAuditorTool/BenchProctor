<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Support\Facades\DB;

class BenchmarkTest00010Controller
{
    public function __invoke()
    {
        $userInput = DB::selectOne('SELECT text FROM comments LIMIT 1')->text;
        $form = new class($userInput) { public function __construct(public readonly string $payload) {} };
        $data = $form->payload;
        simplexml_load_string($data, 'SimpleXMLElement', LIBXML_NONET);
        return response()->json(['ok' => 1]);
    }
}
