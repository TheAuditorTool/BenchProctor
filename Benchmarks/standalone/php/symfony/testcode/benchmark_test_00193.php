<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00193', methods: ['POST'])]
class BenchmarkTest00193Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('Authorization', '');
        $data = vsprintf('%1$s', [$userInput]);
        $checkedPath = '/var/app/data/' . basename($data);
        unlink((string)$checkedPath);
        return new JsonResponse(["committed" => true]);
    }
}
