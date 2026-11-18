// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { PrismaClient } from "@prisma/client";

export const resolveRoster = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.body.payload as string) || "";
  const parts: string[] = [];
  for (const token of String(summary).split(',')) { parts.push(token); }
  const restock: string = parts.join(',');
  if (!/^[a-zA-Z0-9_.#\-]+$/.test(restock)) { res.status(400).json({error:"invalid"}); return; }
  const backorder = restock;
  const _prisma = ((globalThis as unknown as { _prisma?: InstanceType<typeof PrismaClient> })._prisma ??= new PrismaClient());
  await _prisma.$queryRawUnsafe("SELECT * FROM users WHERE id = '" + backorder + "'");
  res.json({ accepted: true });
}
