<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00103', methods: ['POST'])]
class BenchmarkTest00103Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->cookies->get('session_token', '');
        $data = hex2bin($userInput);
        $quotedArg = escapeshellarg((string)$data);
        exec('tar -czf /tmp/backup.tgz ' . (string)$quotedArg);
        return new JsonResponse(["committed" => true]);
    }
}
