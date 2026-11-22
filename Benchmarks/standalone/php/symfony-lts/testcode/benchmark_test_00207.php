<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00207', methods: ['POST'])]
class BenchmarkTest00207Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->request->get('field', '');
        $pending = explode(',', $userInput);
        $data = '';
        while (count($pending)) { $data = array_shift($pending); }
        $sessionCookie = \Symfony\Component\HttpFoundation\Cookie::create('session')->withValue((string)$data)->withPath('/')->withSecure(false)->withHttpOnly(true)->withSameSite('strict');
        $resp = new JsonResponse(['ok' => 1]);
        $resp->headers->setCookie($sessionCookie);
        return $resp;
    }
}
