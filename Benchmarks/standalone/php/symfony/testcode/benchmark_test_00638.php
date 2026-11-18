<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00638', methods: ['POST'])]
class BenchmarkTest00638Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->request->get('field', '');
        if (!in_array((string)$userInput, ['ls', 'cat', 'date', 'whoami'], true)) { return new JsonResponse(['error' => 'forbidden'], 403); }
        $allowedBin = (string)$userInput;
        exec('tar -czf /tmp/backup.tgz ' . (string)$allowedBin);
        return new JsonResponse(["committed" => true]);
    }
}
