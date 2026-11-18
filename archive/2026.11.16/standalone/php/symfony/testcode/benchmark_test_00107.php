<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00107', methods: ['POST'])]
class BenchmarkTest00107Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->request->get('field', '');
        if (!preg_match('#^[a-zA-Z0-9 _.\\#%\\-]+$#', $userInput)) { error_log('input validation failed'); return new JsonResponse(['error'=>'invalid'], 400); }
        $processed = $userInput;
        return new Response('<div>' . $processed . '</div>', 200, ['Content-Type' => 'text/html']);
    }
}
