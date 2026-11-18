<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00558', methods: ['POST'])]
class BenchmarkTest00558Controller
{
    public function __invoke(Request $request)
    {
        $userInput = json_decode($request->getContent(), true)['variables']['input'] ?? '';
        $data = (!empty($userInput)) ? $userInput : '';
        $resp = new JsonResponse(['ok' => 1]);
        $resp->headers->setCookie(\Symfony\Component\HttpFoundation\Cookie::create('session', (string)$data, 0, '/', null, false, true, false, 'Strict'));
        return $resp;
    }
}
