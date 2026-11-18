<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00692', methods: ['POST'])]
class BenchmarkTest00692Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('User-Agent', '');
        exec('tar -czf /tmp/backup.tgz ' . (string)$userInput);
        return new JsonResponse(["committed" => true]);
    }
}
