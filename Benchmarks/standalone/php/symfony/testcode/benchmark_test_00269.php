<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00269', methods: ['POST'])]
class BenchmarkTest00269Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('Authorization', '');
        $asText = function ($v): string { return trim((string) $v); };
        $data = $asText($userInput);
        exec('tar -czf /tmp/backup.tgz ' . (string)$data);
        return new JsonResponse(["committed" => true]);
    }
}
