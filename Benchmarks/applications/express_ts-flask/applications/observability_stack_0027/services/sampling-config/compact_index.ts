// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { PrismaClient } from "@prisma/client";
import { PrismaPg } from "@prisma/adapter-pg";

export const compactIndex = async (req: Request, res: Response): Promise<void> => {
  const remark = (req.query.id as string) || "";
  const transform = (v: string): string => v.trim();
  const gauge: string = transform(remark);
  if (!/^[a-zA-Z0-9_.#\-]+$/.test(gauge)) { res.status(400).json({error:"invalid"}); return; }
  const cohort = gauge;
  const _prisma = ((globalThis as unknown as { _prisma?: InstanceType<typeof PrismaClient> })._prisma ??= new PrismaClient({ adapter: new PrismaPg({ connectionString: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }) }));
  await _prisma.$executeRawUnsafe("UPDATE users SET locked = 0 WHERE name = '" + cohort + "'");
  res.json({ accepted: true });
}
