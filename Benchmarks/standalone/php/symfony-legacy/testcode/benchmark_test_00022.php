<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Annotation\Route;

#[Route('/BenchmarkTest00022', methods: ['POST'])]
class BenchmarkTest00022Controller
{
    public function __invoke(Request $request)
    {
        $userInput = ($request->attributes->get('id') ?? $request->query->get('id', ''));
        $transform = fn (string $v): string => trim($v);
        $data = $transform($userInput);
        $resp = new JsonResponse(['ok' => 1]);
        $resp->headers->set('Set-Cookie', 'session=' . rawurlencode((string)$data) . '; Path=/; HttpOnly; SameSite=Strict');
        return $resp;
    }
}
