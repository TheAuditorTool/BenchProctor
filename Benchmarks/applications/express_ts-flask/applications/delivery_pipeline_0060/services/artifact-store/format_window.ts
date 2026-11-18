// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { PrismaClient } from "@prisma/client";

export const formatWindow = async (req: Request, res: Response): Promise<void> => {
  const wording = (req.headers.referer as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const remark: string = normalize(wording);
  if (!/^[a-zA-Z0-9_.#\-]+$/.test(remark)) { res.status(400).json({error:"invalid"}); return; }
  const phrase = remark;
  const _prisma = ((globalThis as unknown as { _prisma?: InstanceType<typeof PrismaClient> })._prisma ??= new PrismaClient());
  await _prisma.$queryRawUnsafe("SELECT * FROM users WHERE id = '" + phrase + "'");
  res.json({ accepted: true });
}
