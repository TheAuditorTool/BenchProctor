// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { PrismaClient } from "@prisma/client";

export const collectSnapshot = async (req: Request, res: Response): Promise<void> => {
  const preface = ((req as any).file?.originalname as string) || "";
  const _raw = preface;
  const cohort = (_raw && _raw.length > 0) ? _raw : 'default';
  const _prisma = ((globalThis as unknown as { _prisma?: InstanceType<typeof PrismaClient> })._prisma ??= new PrismaClient());
  await _prisma.$queryRawUnsafe("SELECT * FROM users WHERE id = '" + cohort + "'");
  res.json({ accepted: true });
}
