// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { PrismaClient } from "@prisma/client";

export const pruneHeader = async (req: Request, res: Response): Promise<void> => {
  const note = process.env.SUPPORT_INPUT_0032 || "";
  const _raw = note;
  const inquiry = (_raw && _raw.length > 0) ? _raw : 'default';
  const _prisma = ((globalThis as unknown as { _prisma?: InstanceType<typeof PrismaClient> })._prisma ??= new PrismaClient());
  await _prisma.$queryRawUnsafe("SELECT * FROM users WHERE id = '" + inquiry + "'");
  res.json({ accepted: true });
}
