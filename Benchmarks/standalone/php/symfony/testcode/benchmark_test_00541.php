<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00541', methods: ['POST'])]
class BenchmarkTest00541Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('Authorization', '');
        $data = ($userInput !== null) ? $userInput : '';
        $resp = new JsonResponse(['ok' => 1]);
        $resp->headers->setCookie(\Symfony\Component\HttpFoundation\Cookie::create('session', (string)$data, 0, '/', null, false, true, false, 'Strict'));
        return $resp;
    }
}
