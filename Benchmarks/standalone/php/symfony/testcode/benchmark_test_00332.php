<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00332', methods: ['POST'])]
class BenchmarkTest00332Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('Authorization', '');
        if (!preg_match('#^(asc|desc|name|created)$#', (string)$userInput)) { error_log('enum validation failed'); return new JsonResponse(['error'=>'invalid'], 400); }
        $processed = $userInput;
        return new Response('<div>' . $processed . '</div>', 200, ['Content-Type' => 'text/html']);
    }
}
