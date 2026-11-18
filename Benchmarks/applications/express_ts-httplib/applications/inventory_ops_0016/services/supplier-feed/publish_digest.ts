// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import { PrismaClient } from "@prisma/client";

export const publishDigest = async (req: Request, res: Response): Promise<void> => {
  const citation = fs.readFileSync("/tmp/data", "utf8");
  const transform = (v: string): string => v.trim();
  const backorder: string = transform(citation);
  if (!/^[a-zA-Z0-9_.#\-]+$/.test(backorder)) { res.status(400).json({error:"invalid"}); return; }
  const restock = backorder;
  const _prisma = ((globalThis as unknown as { _prisma?: InstanceType<typeof PrismaClient> })._prisma ??= new PrismaClient());
  await _prisma.$queryRawUnsafe("SELECT * FROM users WHERE id = '" + restock + "'");
  res.json({ accepted: true });
}
