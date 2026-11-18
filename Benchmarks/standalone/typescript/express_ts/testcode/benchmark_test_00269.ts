// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { PrismaClient } from "@prisma/client";

export const BenchmarkTest00269 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body as string) || "";
  const [data] = String(userInput).split(',');
  const _prisma = new PrismaClient();
  await _prisma.$queryRawUnsafe("SELECT * FROM users WHERE id = '" + data + "'");
  res.json({ accepted: true });
}
