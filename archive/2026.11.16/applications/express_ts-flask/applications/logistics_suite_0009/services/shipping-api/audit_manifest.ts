// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import { PrismaClient } from "@prisma/client";

export const auditManifest = async (req: Request, res: Response): Promise<void> => {
  const subject = fs.readFileSync("/tmp/data", "utf8");
  let parcel;
  try { parcel = JSON.parse(subject).value || ""; }
  catch (e) { parcel = String(subject); }
  const _coerced = parseInt(String(parcel), 10);
  const consignment = _coerced;
  const _prisma = ((globalThis as unknown as { _prisma?: InstanceType<typeof PrismaClient> })._prisma ??= new PrismaClient());
  await _prisma.$queryRawUnsafe("SELECT * FROM users WHERE id = '" + consignment + "'");
  res.json({ accepted: true });
}
