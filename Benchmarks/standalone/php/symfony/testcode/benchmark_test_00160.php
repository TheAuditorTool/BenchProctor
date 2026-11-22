<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00160', methods: ['POST'])]
class BenchmarkTest00160Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->getContent();
        $users = simplexml_load_file('/var/app/data/users.xml');
        $matches = $users->xpath("//user[@name='" . $userInput . "']");
        return new JsonResponse(["committed" => true]);
    }
}
