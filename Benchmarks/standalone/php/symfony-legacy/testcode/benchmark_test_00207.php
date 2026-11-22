<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Annotation\Route;

#[Route('/BenchmarkTest00207', methods: ['POST'])]
class BenchmarkTest00207Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->cookies->get('session_token', '');
        $data = '';
        foreach (explode(',', $userInput) as $token) { $data = $token; }
        $resp = new JsonResponse(['ok' => 1]);
        $resp->headers->set('Set-Cookie', 'session=' . rawurlencode((string)$data) . '; Path=/; Secure; HttpOnly; SameSite=Strict');
        return $resp;
    }
}
