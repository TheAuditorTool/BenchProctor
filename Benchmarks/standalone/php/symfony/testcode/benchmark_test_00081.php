<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00081', methods: ['POST'])]
class BenchmarkTest00081Controller
{
    public function __invoke(Connection $conn)
    {
        $userInput = $conn->fetchOne('SELECT text FROM comments LIMIT 1');
        $data = str_replace("\0", '', $userInput);
        $records = (int) $data;
        $frame = str_repeat("\0", (int) ($records * 16));
        return new JsonResponse(['frame_bytes' => strlen($frame)], 200);
    }
}
