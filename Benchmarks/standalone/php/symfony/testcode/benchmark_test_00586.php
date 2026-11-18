<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00586', methods: ['POST'])]
class BenchmarkTest00586Controller
{
    public function __invoke(Request $request)
    {
        $userInput = ($request->attributes->get('id') ?? $request->query->get('id', ''));
        $words = preg_split('/\s+/', $userInput);
        $data = implode(' ', $words);
        if (!preg_match('#^[a-zA-Z0-9 _.\\#~\\-]+$#', $data)) { error_log('input validation failed'); return new JsonResponse(['error'=>'invalid'], 400); }
        $processed = $data;
        unlink('/var/app/data/' . $processed);
        return new JsonResponse(["committed" => true]);
    }
}
