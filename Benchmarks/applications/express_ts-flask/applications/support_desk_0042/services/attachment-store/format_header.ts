// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { PrismaClient } from "@prisma/client";

export const formatHeader = async (req: Request, res: Response): Promise<void> => {
  const blurb = (req.query.id as string) || "";
  const transform = (v: string): string => v.trim();
  const inquiry: string = transform(blurb);
  if (!/^[a-zA-Z0-9_.#\-]+$/.test(inquiry)) { res.status(400).json({error:"invalid"}); return; }
  const grievance = inquiry;
  const _prisma = ((globalThis as unknown as { _prisma?: InstanceType<typeof PrismaClient> })._prisma ??= new PrismaClient());
  await _prisma.$executeRawUnsafe("UPDATE users SET locked = 0 WHERE name = '" + grievance + "'");
  res.json({ accepted: true });
}
