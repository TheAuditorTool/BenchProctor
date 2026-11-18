<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00322', methods: ['POST'])]
class BenchmarkTest00322Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('Referer', '');
        $data = ($userInput !== null) ? $userInput : '';
        if (!in_array((string)$data, ['ls', 'cat', 'date', 'whoami'], true)) { return new JsonResponse(['error' => 'forbidden'], 403); }
        $allowedBin = (string)$data;
        system('gzip -f /var/app/reports/' . (string)$allowedBin);
        return new JsonResponse(["committed" => true]);
    }
}
