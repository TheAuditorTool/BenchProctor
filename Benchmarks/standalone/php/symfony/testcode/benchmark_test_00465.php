<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00465', methods: ['POST'])]
class BenchmarkTest00465Controller
{
    public function __invoke(Request $request)
    {
        $userInput = json_decode($request->getContent(), true)['payload'] ?? '';
        $data = sprintf('%s', $userInput);
        $checkedPath = '/var/app/data/' . basename($data);
        unlink((string)$checkedPath);
        return new JsonResponse(["committed" => true]);
    }
}
