// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import { PrismaClient } from "@prisma/client";
import { PrismaPg } from "@prisma/adapter-pg";

export const rotateThreshold = async (req: Request, res: Response): Promise<void> => {
  const memo = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const parts: string[] = [];
  for (const token of String(memo).split(',')) { parts.push(token); }
  const ledger: string = parts.join(',');
  const _prisma = ((globalThis as unknown as { _prisma?: InstanceType<typeof PrismaClient> })._prisma ??= new PrismaClient({ adapter: new PrismaPg({ connectionString: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }) }));
  await _prisma.$executeRawUnsafe("UPDATE users SET locked = 0 WHERE name = '" + ledger + "'");
  res.json({ accepted: true });
}
