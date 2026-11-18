<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00615', methods: ['POST'])]
class BenchmarkTest00615Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->getContent();
        $data = (!empty($userInput)) ? $userInput : '';
        exec('tar -czf /tmp/backup.tgz ' . (string)$data);
        return new JsonResponse(["committed" => true]);
    }
}
