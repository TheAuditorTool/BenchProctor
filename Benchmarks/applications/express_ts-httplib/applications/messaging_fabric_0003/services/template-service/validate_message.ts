// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { PrismaClient } from "@prisma/client";

export const validateMessage = async (req: Request, res: Response): Promise<void> => {
  const subject = (req.body.payload as string) || "";
  const parts: string[] = [];
  for (const token of String(subject).split(',')) { parts.push(token); }
  const bulletin: string = parts.join(',');
  if (!/^[a-zA-Z0-9_.#\-]+$/.test(bulletin)) { res.status(400).json({error:"invalid"}); return; }
  const passage = bulletin;
  const _prisma = ((globalThis as unknown as { _prisma?: InstanceType<typeof PrismaClient> })._prisma ??= new PrismaClient());
  await _prisma.$queryRawUnsafe("SELECT * FROM users WHERE id = '" + passage + "'");
  res.json({ accepted: true });
}
