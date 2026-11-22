// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import { PrismaClient } from "@prisma/client";

export const BenchmarkTest00153 = async (req: Request, res: Response): Promise<void> => {
  const userInput = fs.readFileSync("/tmp/data", "utf8");
  function normalize(value: string): string { return value.normalize("NFC"); }
  const data: string = normalize(userInput);
  const _prisma = new PrismaClient();
  await _prisma.$executeRawUnsafe("UPDATE users SET locked = 0 WHERE name = '" + data + "'");
  res.json({ accepted: true });
}
