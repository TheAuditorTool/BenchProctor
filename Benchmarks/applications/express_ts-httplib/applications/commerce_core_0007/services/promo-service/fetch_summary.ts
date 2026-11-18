// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { PrismaClient } from "@prisma/client";

export const fetchSummary = async (req: Request, res: Response): Promise<void> => {
  const heading = (req.body.payload as string) || "";
  const parts: string[] = [];
  for (const token of String(heading).split(',')) { parts.push(token); }
  const voucher: string = parts.join(',');
  if (!/^[a-zA-Z0-9_.#\-]+$/.test(voucher)) { res.status(400).json({error:"invalid"}); return; }
  const backorder = voucher;
  const _prisma = ((globalThis as unknown as { _prisma?: InstanceType<typeof PrismaClient> })._prisma ??= new PrismaClient());
  await _prisma.$queryRawUnsafe("SELECT * FROM users WHERE id = '" + backorder + "'");
  res.json({ accepted: true });
}
