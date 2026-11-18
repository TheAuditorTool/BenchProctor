<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00330', methods: ['POST'])]
class BenchmarkTest00330Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('Referer', '');
        $data = strtr('{0}', ['{0}' => (string)$userInput]);
        $resolved = realpath('/var/app/data/' . $data);
        if ($resolved === false || strpos($resolved, '/var/app/data/') !== 0) { return new JsonResponse(['error'=>'forbidden'], 403); }
        $checkedPath = $resolved;
        $content = file_get_contents($checkedPath);
        return new JsonResponse(["committed" => true]);
    }
}
