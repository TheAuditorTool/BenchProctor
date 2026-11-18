<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00040', methods: ['POST'])]
class BenchmarkTest00040Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->cookies->get('session_token', '');
        $data = hex2bin($userInput);
        $resolved = realpath('/var/app/data/' . $data);
        if ($resolved === false || strpos($resolved, '/var/app/data/') !== 0) { return new JsonResponse(['error'=>'forbidden'], 403); }
        $checkedPath = $resolved;
        file_put_contents((string)$checkedPath, 'data');
        return new JsonResponse(["committed" => true]);
    }
}
