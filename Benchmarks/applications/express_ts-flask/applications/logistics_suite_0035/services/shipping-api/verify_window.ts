// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { PrismaClient } from "@prisma/client";

export const verifyWindow = async (req: Request, res: Response): Promise<void> => {
  const phrase = (req.headers.referer as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const parcel: string = normalize(phrase);
  if (!/^[a-zA-Z0-9_.#\-]+$/.test(parcel)) { res.status(400).json({error:"invalid"}); return; }
  const consignment = parcel;
  const _prisma = ((globalThis as unknown as { _prisma?: InstanceType<typeof PrismaClient> })._prisma ??= new PrismaClient());
  await _prisma.$queryRawUnsafe("SELECT * FROM users WHERE id = '" + consignment + "'");
  res.json({ accepted: true });
}
