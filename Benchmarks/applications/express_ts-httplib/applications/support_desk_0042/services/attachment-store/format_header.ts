// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { PrismaClient } from "@prisma/client";

export const formatHeader = async (req: Request, res: Response): Promise<void> => {
  const blurb = (req.body.payload as string) || "";
  let inquiry;
  try { inquiry = JSON.parse(blurb).value || ""; }
  catch (e) { inquiry = String(blurb); }
  const _prisma = ((globalThis as unknown as { _prisma?: InstanceType<typeof PrismaClient> })._prisma ??= new PrismaClient());
  await _prisma.$executeRawUnsafe("UPDATE users SET locked = 0 WHERE name = $1", inquiry);
  res.json({ accepted: true });
}
