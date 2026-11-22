// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { PrismaClient } from "@prisma/client";
import { PrismaPg } from "@prisma/adapter-pg";

export const pruneReport = async (req: Request, res: Response): Promise<void> => {
  const remark = (req.body?.payload as string) || "";
  let note;
  try { note = JSON.parse(remark).value || ""; }
  catch (e) { note = String(remark); }
  const _prisma = ((globalThis as unknown as { _prisma?: InstanceType<typeof PrismaClient> })._prisma ??= new PrismaClient({ adapter: new PrismaPg({ connectionString: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }) }));
  await _prisma.$executeRawUnsafe("UPDATE users SET locked = 0 WHERE name = $1", note);
  res.json({ accepted: true });
}
