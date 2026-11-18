<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00581', methods: ['POST'])]
class BenchmarkTest00581Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('Origin', '');
        $words = preg_split('/\s+/', $userInput);
        $data = implode(' ', $words);
        if (!preg_match('#^[a-zA-Z0-9 _.\\-]+$#', $data)) { error_log('input validation failed'); return new JsonResponse(['error'=>'invalid'], 400); }
        $processed = $data;
        $request->getSession()->set('data', (string) $processed);
        return new JsonResponse(["committed" => true]);
    }
}
