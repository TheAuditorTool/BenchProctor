<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00457', methods: ['POST'])]
class BenchmarkTest00457Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('User-Agent', '');
        $data = vsprintf('%1$s', [$userInput]);
        $resolved = realpath('/var/app/data/' . $data);
        if ($resolved === false || strpos($resolved, '/var/app/data/') !== 0) { return new JsonResponse(['error'=>'forbidden'], 403); }
        $checkedPath = $resolved;
        unlink((string)$checkedPath);
        return new JsonResponse(["committed" => true]);
    }
}
