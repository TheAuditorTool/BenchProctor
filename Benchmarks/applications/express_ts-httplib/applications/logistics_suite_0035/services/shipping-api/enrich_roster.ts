// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import { PrismaClient } from "@prisma/client";

export const enrichRoster = async (req: Request, res: Response): Promise<void> => {
  const phrase = fs.readFileSync("/tmp/data", "utf8");
  const transform = (v: string): string => v.trim();
  const parcel: string = transform(phrase);
  if (!/^[a-zA-Z0-9_.#\-]+$/.test(parcel)) { res.status(400).json({error:"invalid"}); return; }
  const consignment = parcel;
  const _prisma = ((globalThis as unknown as { _prisma?: InstanceType<typeof PrismaClient> })._prisma ??= new PrismaClient());
  await _prisma.$queryRawUnsafe("SELECT * FROM users WHERE id = '" + consignment + "'");
  res.json({ accepted: true });
}
