<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00129', methods: ['POST'])]
class BenchmarkTest00129Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('X-Custom-Header', '');
        $words = preg_split('/\s+/', $userInput);
        $data = implode(' ', $words);
        $resp = new JsonResponse(['ok' => 1]);
        $resp->headers->set('Set-Cookie', 'session=' . rawurlencode((string)$data) . '; Path=/; HttpOnly; SameSite=Strict');
        return $resp;
    }
}
