<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Annotation\Route;

#[Route('/BenchmarkTest00016', methods: ['POST'])]
class BenchmarkTest00016Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('Origin', '');
        $data = str_replace("\0", '', $userInput);
        $sessionCookie = \Symfony\Component\HttpFoundation\Cookie::create('session')->withValue((string)$data)->withPath('/')->withSecure(true)->withHttpOnly(true)->withSameSite('strict');
        $resp = new JsonResponse(['ok' => 1]);
        $resp->headers->setCookie($sessionCookie);
        return $resp;
    }
}
