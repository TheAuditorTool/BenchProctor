<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00022', methods: ['POST'])]
class BenchmarkTest00022Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->cookies->get('session_token', '');
        $form = new class($userInput) { public function __construct(public readonly string $payload) {} };
        $data = $form->payload;
        $sessionCookie = \Symfony\Component\HttpFoundation\Cookie::create('session')->withValue((string)$data)->withPath('/')->withSecure(true)->withHttpOnly(true)->withSameSite('strict');
        $resp = new JsonResponse(['ok' => 1]);
        $resp->headers->setCookie($sessionCookie);
        return $resp;
    }
}
