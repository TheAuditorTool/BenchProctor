<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00088', methods: ['POST'])]
class BenchmarkTest00088Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('Referer', '');
        $data = sprintf('%s', $userInput);
        $quotedArg = escapeshellarg((string)$data);
        exec('tar -czf /tmp/backup.tgz ' . (string)$quotedArg);
        return new JsonResponse(["committed" => true]);
    }
}
