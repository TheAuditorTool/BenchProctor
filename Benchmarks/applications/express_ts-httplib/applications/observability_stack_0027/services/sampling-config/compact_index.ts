// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { PrismaClient } from "@prisma/client";

export const compactIndex = async (req: Request, res: Response): Promise<void> => {
  const remark = (req.body.payload as string) || "";
  let gauge;
  try { gauge = JSON.parse(remark).value || ""; }
  catch (e) { gauge = String(remark); }
  const _prisma = ((globalThis as unknown as { _prisma?: InstanceType<typeof PrismaClient> })._prisma ??= new PrismaClient());
  await _prisma.$executeRawUnsafe("UPDATE users SET locked = 0 WHERE name = $1", gauge);
  res.json({ accepted: true });
}
