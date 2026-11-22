<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Support\Facades\DB;

class BenchmarkTest00311Controller
{
    public function __invoke()
    {
        $userInput = DB::selectOne('SELECT text FROM comments LIMIT 1')->text;
        $transform = fn (string $v): string => trim($v);
        $data = $transform($userInput);
        $compiled = tempnam('/var/app/cache', 'rule_');
        file_put_contents($compiled, '<?php return static fn (array $order) => ' . $data . ';');
        $rule = include $compiled;
        unlink($compiled);
        $result = $rule(['total' => 100, 'items' => 3]);
        return response()->json(['ok' => 1]);
    }
}
