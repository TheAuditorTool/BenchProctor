<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00138', methods: ['POST'])]
class BenchmarkTest00138Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('Host', '');
        $transform = fn (string $v): string => trim($v);
        $data = $transform($userInput);
        $_coerced = (float)$data;
        $processed = $_coerced;
        $users = simplexml_load_file('/var/app/data/users.xml');
        $matches = $users->xpath("//user[@name='" . $processed . "']");
        return new JsonResponse(["committed" => true]);
    }
}
