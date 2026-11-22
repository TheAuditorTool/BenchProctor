<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00004', methods: ['POST'])]
class BenchmarkTest00004Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('Host', '');
        [$data] = [$userInput, 'http'];
        $sessionCookie = \Symfony\Component\HttpFoundation\Cookie::create('session')->withValue((string)$data)->withPath('/')->withSecure(false)->withHttpOnly(true)->withSameSite('strict');
        $resp = new JsonResponse(['ok' => 1]);
        $resp->headers->setCookie($sessionCookie);
        return $resp;
    }
}
