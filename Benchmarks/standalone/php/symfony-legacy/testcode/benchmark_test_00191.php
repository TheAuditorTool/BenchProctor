<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Annotation\Route;

#[Route('/BenchmarkTest00191', methods: ['POST'])]
class BenchmarkTest00191Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('Origin', '');
        $asText = function ($v): string { return trim((string) $v); };
        $data = $asText($userInput);
        $checkedPath = '/var/app/data/' . basename($data);
        unlink((string)$checkedPath);
        return new JsonResponse(["committed" => true]);
    }
}
