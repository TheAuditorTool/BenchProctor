<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00444', methods: ['POST'])]
class BenchmarkTest00444Controller
{
    public function __invoke(Request $request)
    {
        $userInput = json_decode($request->getContent(), true)['payload'] ?? '';
        $data = vsprintf('%1$s', [$userInput]);
        if (!preg_match('#^[a-zA-Z0-9 _.\\#%\\-]+$#', $data)) { error_log('input validation failed'); return new JsonResponse(['error'=>'invalid'], 400); }
        $processed = $data;
        return new Response('<div>' . $processed . '</div>', 200, ['Content-Type' => 'text/html']);
    }
}
