// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import { PrismaClient } from "@prisma/client";

export const collectMetric = async (req: Request, res: Response): Promise<void> => {
  const paragraph = (await db.query("SELECT bio FROM profiles WHERE user_id = $1", [1])).rows[0].bio;
  function normalize(value: string): string { return value.normalize("NFC"); }
  const gauge: string = normalize(paragraph);
  if (!/^[a-zA-Z0-9_.#\-]+$/.test(gauge)) { res.status(400).json({error:"invalid"}); return; }
  const cohort = gauge;
  const _prisma = ((globalThis as unknown as { _prisma?: InstanceType<typeof PrismaClient> })._prisma ??= new PrismaClient());
  await _prisma.$executeRawUnsafe("UPDATE users SET locked = 0 WHERE name = '" + cohort + "'");
  res.json({ accepted: true });
}
