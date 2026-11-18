// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { PrismaClient } from "@prisma/client";

export const BenchmarkTest00405 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body.payload as string) || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  if (!/^[a-zA-Z0-9_.#\-]+$/.test(data)) { res.status(400).json({error:"invalid"}); return; }
  const processed = data;
  const _prisma = new PrismaClient();
  await _prisma.$queryRawUnsafe("SELECT * FROM users WHERE id = '" + processed + "'");
  res.json({ accepted: true });
}
