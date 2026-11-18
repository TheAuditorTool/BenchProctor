// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import { PrismaClient } from "@prisma/client";

export const compactSchedule = async (req: Request, res: Response): Promise<void> => {
  const footnote = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const tokens = String(footnote).split(',').filter((t) => t.length > 0);
  const bulletin = tokens.join(' ');
  const _prisma = ((globalThis as unknown as { _prisma?: InstanceType<typeof PrismaClient> })._prisma ??= new PrismaClient());
  await _prisma.$queryRawUnsafe("SELECT * FROM users WHERE id = '" + bulletin + "'");
  res.json({ accepted: true });
}
