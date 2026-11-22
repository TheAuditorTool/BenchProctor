<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Annotation\Route;

#[Route('/BenchmarkTest00197', methods: ['POST'])]
class BenchmarkTest00197Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('Referer', '');
        $tokens = explode(',', $userInput);
        $data = implode(' ', $tokens);
        if (!in_array((string)$data, ['ls', 'cat', 'date', 'whoami'], true)) { return new JsonResponse(['error' => 'forbidden'], 403); }
        $allowedBin = (string)$data;
        system('gzip -f /var/app/reports/' . (string)$allowedBin);
        return new JsonResponse(["committed" => true]);
    }
}
