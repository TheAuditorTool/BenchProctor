<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Annotation\Route;

#[Route('/BenchmarkTest00183', methods: ['POST'])]
class BenchmarkTest00183Controller
{
    public function __invoke(Request $request)
    {
        $userInput = json_decode($request->getContent(), true)['payload'] ?? '';
        $data = sprintf('%s', $userInput);
        $macKey = (string) getenv('PAYLOAD_MAC_KEY');
        [$mac, $serialized] = array_pad(explode('.', (string)$data, 2), 2, '');
        if ($macKey === '' || !hash_equals(hash_hmac('sha256', $serialized, $macKey), $mac)) { return new JsonResponse(['error' => 'payload signature mismatch'], 403); }
        unserialize($serialized);
        return new JsonResponse(["committed" => true]);
    }
}
