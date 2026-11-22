<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00084', methods: ['POST'])]
class BenchmarkTest00084Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('Authorization', '');
        $data = ($userInput !== null) ? $userInput : '';
        $resp = new JsonResponse(['ok' => 1]);
        $resp->headers->set('Set-Cookie', 'session=' . rawurlencode((string)$data) . '; Path=/; Secure; HttpOnly; SameSite=Strict');
        return $resp;
    }
}
