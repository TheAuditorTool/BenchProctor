// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { PrismaClient } from "@prisma/client";

export const renderReport = async (req: Request, res: Response): Promise<void> => {
  const heading = (req.headers.referer as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const voucher: string = normalize(heading);
  const _prisma = ((globalThis as unknown as { _prisma?: InstanceType<typeof PrismaClient> })._prisma ??= new PrismaClient());
  await _prisma.user.findUnique({ where: { id: Number(voucher) } });
  res.json({ accepted: true });
}
