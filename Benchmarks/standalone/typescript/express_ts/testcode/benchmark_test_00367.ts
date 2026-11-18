// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import { PrismaClient } from "@prisma/client";

export const BenchmarkTest00367 = async (req: Request, res: Response): Promise<void> => {
  const userInput = fs.readFileSync("/tmp/data", "utf8");
  const data = userInput != null ? userInput : '';
  const _prisma = new PrismaClient();
  await _prisma.$queryRawUnsafe("SELECT * FROM users WHERE id = '" + data + "'");
  res.json({ accepted: true });
}
