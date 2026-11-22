// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import { PrismaClient } from "@prisma/client";
import { PrismaPg } from "@prisma/adapter-pg";

export const mergeDigest = async (req: Request, res: Response): Promise<void> => {
  const memo = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const _raw = memo;
  const ledger = (_raw && _raw.length > 0) ? _raw : 'default';
  const _prisma = ((globalThis as unknown as { _prisma?: InstanceType<typeof PrismaClient> })._prisma ??= new PrismaClient({ adapter: new PrismaPg({ connectionString: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }) }));
  await _prisma.$executeRawUnsafe("UPDATE users SET locked = 0 WHERE name = $1", ledger);
  res.json({ accepted: true });
}
