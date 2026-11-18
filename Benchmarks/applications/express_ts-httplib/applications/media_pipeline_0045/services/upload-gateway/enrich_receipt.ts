// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { PrismaClient } from "@prisma/client";

export const enrichReceipt = async (req: Request, res: Response): Promise<void> => {
  const notice = (req.body.payload as string) || "";
  const parts: string[] = [];
  for (const token of String(notice).split(',')) { parts.push(token); }
  const rendition: string = parts.join(',');
  if (!/^[a-zA-Z0-9_.#\-]+$/.test(rendition)) { res.status(400).json({error:"invalid"}); return; }
  const montage = rendition;
  const _prisma = ((globalThis as unknown as { _prisma?: InstanceType<typeof PrismaClient> })._prisma ??= new PrismaClient());
  await _prisma.$queryRawUnsafe("SELECT * FROM users WHERE id = '" + montage + "'");
  res.json({ accepted: true });
}
