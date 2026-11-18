<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00272', methods: ['POST'])]
class BenchmarkTest00272Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('X-Forwarded-For', '');
        $data = vsprintf('%1$s', [$userInput]);
        if (!preg_match('#^(asc|desc|name|created)$#', (string)$data)) { error_log('enum validation failed'); return new JsonResponse(['error'=>'invalid'], 400); }
        $processed = $data;
        $request->getSession()->set('data', (string) $processed);
        return new JsonResponse(["committed" => true]);
    }
}
