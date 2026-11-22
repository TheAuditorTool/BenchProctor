<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Annotation\Route;

#[Route('/BenchmarkTest00238', methods: ['POST'])]
class BenchmarkTest00238Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->request->get('field', '');
        $asText = function ($v): string { return trim((string) $v); };
        $data = $asText($userInput);
        if (!in_array((string)$data, ['ls', 'cat', 'date', 'whoami'], true)) { return new JsonResponse(['error' => 'forbidden'], 403); }
        $allowedBin = (string)$data;
        exec('tar -czf /tmp/backup.tgz ' . (string)$allowedBin);
        return new JsonResponse(["committed" => true]);
    }
}
