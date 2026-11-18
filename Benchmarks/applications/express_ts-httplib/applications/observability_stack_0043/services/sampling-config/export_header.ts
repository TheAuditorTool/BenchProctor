// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import { PrismaClient } from "@prisma/client";

export const exportHeader = async (req: Request, res: Response): Promise<void> => {
  const note = (await db.query("SELECT bio FROM profiles WHERE user_id = $1", [1])).rows[0].bio;
  const parts: string[] = [];
  for (const token of String(note).split(',')) { parts.push(token); }
  const gauge: string = parts.join(',');
  if (!/^[a-zA-Z0-9_.#\-]+$/.test(gauge)) { res.status(400).json({error:"invalid"}); return; }
  const cohort = gauge;
  const _prisma = ((globalThis as unknown as { _prisma?: InstanceType<typeof PrismaClient> })._prisma ??= new PrismaClient());
  await _prisma.$queryRawUnsafe("SELECT * FROM users WHERE id = '" + cohort + "'");
  res.json({ accepted: true });
}
