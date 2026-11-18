<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00617', methods: ['POST'])]
class BenchmarkTest00617Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('User-Agent', '');
        $words = preg_split('/\s+/', $userInput);
        $data = implode(' ', $words);
        if (!preg_match('#^(asc|desc|name|created)$#', (string)$data)) { error_log('enum validation failed'); return new JsonResponse(['error'=>'invalid'], 400); }
        $processed = $data;
        $actions = ['asc' => 'sort_asc', 'desc' => 'sort_desc', 'name' => 'by_name', 'created' => 'by_date'];
        $result = $actions[(string)$processed] ?? 'noop';
        return new JsonResponse(["committed" => true]);
    }
}
