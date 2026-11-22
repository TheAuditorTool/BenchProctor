<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Annotation\Route;

#[Route('/BenchmarkTest00169', methods: ['POST'])]
class BenchmarkTest00169Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->request->get('multipart_field', '');
        $pending = explode(',', $userInput);
        $data = '';
        while (count($pending)) { $data = array_shift($pending); }
        $zones = ['utc' => new \DateTimeZone('UTC'), 'berlin' => new \DateTimeZone('Europe/Berlin'), 'tokyo' => new \DateTimeZone('Asia/Tokyo')];
        $zone = $zones[(string)$data] ?? null;
        if ($zone === null) { return new JsonResponse(["error" => "not found"], 404); }
        $zoneName = $zone->getName();
        return new JsonResponse(["committed" => true]);
    }
}
