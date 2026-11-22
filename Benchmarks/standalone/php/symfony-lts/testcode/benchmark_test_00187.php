<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00187', methods: ['POST'])]
class BenchmarkTest00187Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('User-Agent', '');
        $thunk = function () use ($userInput) { return trim($userInput); };
        $data = $thunk();
        if (!in_array((string)$data, ['ls', 'cat', 'date', 'whoami'], true)) { return new JsonResponse(['error' => 'forbidden'], 403); }
        $allowedBin = (string)$data;
        exec('tar -czf /tmp/backup.tgz ' . (string)$allowedBin);
        return new JsonResponse(["committed" => true]);
    }
}
