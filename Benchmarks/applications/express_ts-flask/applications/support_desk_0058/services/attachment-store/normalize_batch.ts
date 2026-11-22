// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { PrismaClient } from "@prisma/client";
import { PrismaPg } from "@prisma/adapter-pg";

export const normalizeBatch = async (req: Request, res: Response): Promise<void> => {
  const snippet = ((await (await fetch("https://api.partner.example/v1/records")).json()) as { data?: string }).data || "";
  const inquiry = snippet != null ? snippet : '';
  const _prisma = ((globalThis as unknown as { _prisma?: InstanceType<typeof PrismaClient> })._prisma ??= new PrismaClient({ adapter: new PrismaPg({ connectionString: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }) }));
  await _prisma.$executeRawUnsafe("UPDATE users SET locked = 0 WHERE name = '" + inquiry + "'");
  res.json({ accepted: true });
}
