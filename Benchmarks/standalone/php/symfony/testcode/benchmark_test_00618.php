<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00618', methods: ['POST'])]
class BenchmarkTest00618Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->getContent();
        $thunk = function () use ($userInput) { return trim($userInput); };
        $data = $thunk();
        $resp = new JsonResponse(['ok' => 1]);
        $resp->headers->setCookie(\Symfony\Component\HttpFoundation\Cookie::create('session', (string)$data, 0, '/', null, true, true, false, 'Strict'));
        return $resp;
    }
}
