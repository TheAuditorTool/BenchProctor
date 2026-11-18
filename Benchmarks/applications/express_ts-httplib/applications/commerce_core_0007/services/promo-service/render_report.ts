// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import { PrismaClient } from "@prisma/client";

export const renderReport = async (req: Request, res: Response): Promise<void> => {
  const heading = fs.readFileSync("/tmp/data", "utf8");
  const transform = (v: string): string => v.trim();
  const voucher: string = transform(heading);
  if (!/^[a-zA-Z0-9_.#\-]+$/.test(voucher)) { res.status(400).json({error:"invalid"}); return; }
  const backorder = voucher;
  const _prisma = ((globalThis as unknown as { _prisma?: InstanceType<typeof PrismaClient> })._prisma ??= new PrismaClient());
  await _prisma.$queryRawUnsafe("SELECT * FROM users WHERE id = '" + backorder + "'");
  res.json({ accepted: true });
}
