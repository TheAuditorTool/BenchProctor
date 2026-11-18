<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00133', methods: ['POST'])]
class BenchmarkTest00133Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->query->get('id', '');
        $data = "{$userInput}";
        exec('tar -czf /tmp/backup.tgz ' . (string)$data);
        return new JsonResponse(["committed" => true]);
    }
}
