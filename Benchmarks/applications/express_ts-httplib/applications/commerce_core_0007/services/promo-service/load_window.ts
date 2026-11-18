// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { PrismaClient } from "@prisma/client";
import { createClient } from "redis";

export const loadWindow = async (req: Request, res: Response): Promise<void> => {
  const _cache = createClient({ url: "redis://cache:6379" });
  await _cache.connect();
  const heading = (await _cache.get("user_data")) || "";
  const _raw = heading;
  const voucher = (_raw && _raw.length > 0) ? _raw : 'default';
  const _prisma = ((globalThis as unknown as { _prisma?: InstanceType<typeof PrismaClient> })._prisma ??= new PrismaClient());
  await _prisma.$queryRawUnsafe("SELECT * FROM users WHERE id = '" + voucher + "'");
  res.json({ accepted: true });
}
