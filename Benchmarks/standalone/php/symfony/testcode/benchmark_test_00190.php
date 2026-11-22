<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00190', methods: ['POST'])]
class BenchmarkTest00190Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->query->get('id', '');
        [$data] = [$userInput, 'http'];
        $quotedArg = escapeshellarg((string)$data);
        exec('tar -czf /tmp/backup.tgz ' . (string)$quotedArg);
        return new JsonResponse(["committed" => true]);
    }
}
