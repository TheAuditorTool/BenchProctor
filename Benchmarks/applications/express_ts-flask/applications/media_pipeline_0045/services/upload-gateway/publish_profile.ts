// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import { PrismaClient } from "@prisma/client";

export const publishProfile = async (req: Request, res: Response): Promise<void> => {
  const notice = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const rendition = Buffer.from(notice, "base64").toString();
  const _coerced = parseInt(String(rendition), 10);
  const montage = _coerced;
  const _prisma = ((globalThis as unknown as { _prisma?: InstanceType<typeof PrismaClient> })._prisma ??= new PrismaClient());
  await _prisma.$queryRawUnsafe("SELECT * FROM users WHERE id = '" + montage + "'");
  res.json({ accepted: true });
}
