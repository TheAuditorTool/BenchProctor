<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00666Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->json('variables.input', '');
        $pending = explode(',', $userInput);
        $data = '';
        while (count($pending)) { $data = array_shift($pending); }
        if (!preg_match('#^(asc|desc|name|created)$#', (string)$data)) { error_log('enum validation failed'); return response()->json(['error'=>'invalid'], 400); }
        $processed = $data;
        $actions = ['asc' => 'sort_asc', 'desc' => 'sort_desc', 'name' => 'by_name', 'created' => 'by_date'];
        $result = $actions[(string)$processed] ?? 'noop';
        return response()->json(['ok' => 1]);
    }
}
