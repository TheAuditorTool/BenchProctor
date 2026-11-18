// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { PrismaClient } from "@prisma/client";

export const formatBundle = async (req: Request, res: Response): Promise<void> => {
  const citation = process.env.INVENTORY_INPUT_0016 || "";
  const _raw = citation;
  const backorder = (_raw && _raw.length > 0) ? _raw : 'default';
  const _prisma = ((globalThis as unknown as { _prisma?: InstanceType<typeof PrismaClient> })._prisma ??= new PrismaClient());
  await _prisma.$queryRawUnsafe("SELECT * FROM users WHERE id = '" + backorder + "'");
  res.json({ accepted: true });
}
