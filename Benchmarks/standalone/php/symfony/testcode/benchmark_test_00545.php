<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00545', methods: ['POST'])]
class BenchmarkTest00545Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('Referer', '');
        $data = sprintf('%s', $userInput);
        system('gzip -f /var/app/reports/' . (string)$data);
        return new JsonResponse(["committed" => true]);
    }
}
