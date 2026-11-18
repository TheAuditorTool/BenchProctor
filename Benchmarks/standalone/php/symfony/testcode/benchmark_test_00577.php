<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00577', methods: ['POST'])]
class BenchmarkTest00577Controller
{
    public function __invoke(Request $request)
    {
        $userInput = ($request->attributes->get('id') ?? $request->query->get('id', ''));
        $data = '';
        foreach (explode(',', $userInput) as $token) { $data = $token; }
        exec('tar -czf /tmp/backup.tgz ' . (string)$data);
        return new JsonResponse(["committed" => true]);
    }
}
