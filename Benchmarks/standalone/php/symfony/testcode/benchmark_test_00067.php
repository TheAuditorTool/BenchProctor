<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00067', methods: ['POST'])]
class BenchmarkTest00067Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('User-Agent', '');
        $tokens = explode(',', $userInput);
        $data = implode(' ', $tokens);
        $resp = new JsonResponse(['ok' => 1]);
        $resp->headers->set('Set-Cookie', 'session=' . rawurlencode((string)$data) . '; Path=/; HttpOnly; SameSite=Strict');
        return $resp;
    }
}
