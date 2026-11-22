<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00051', methods: ['POST'])]
class BenchmarkTest00051Controller
{
    public function __invoke()
    {
        $userInput = getenv('APP_INPUT') ?: '';
        $data = strtr('{0}', ['{0}' => (string)$userInput]);
        $sessionCookie = \Symfony\Component\HttpFoundation\Cookie::create('session')->withValue((string)$data)->withPath('/')->withSecure(true)->withHttpOnly(true)->withSameSite('strict');
        $resp = new JsonResponse(['ok' => 1]);
        $resp->headers->setCookie($sessionCookie);
        return $resp;
    }
}
