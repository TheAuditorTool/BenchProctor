<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00005', methods: ['POST'])]
class BenchmarkTest00005Controller
{
    public function __invoke()
    {
        $userInput = getenv('APP_INPUT') ?: '';
        $thunk = function () use ($userInput) { return trim($userInput); };
        $data = $thunk();
        if (!preg_match('#^[a-zA-Z0-9 _.%~\\-]+$#', $data)) { error_log('input validation failed'); return new JsonResponse(['error'=>'invalid'], 400); }
        $processed = $data;
        $users = simplexml_load_file('/var/app/data/users.xml');
        $matches = $users->xpath("//user[@name='" . $processed . "']");
        return new JsonResponse(["committed" => true]);
    }
}
