// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import { PrismaClient } from "@prisma/client";

export const summarizeCheckpoint = async (req: Request, res: Response): Promise<void> => {
  const excerpt = fs.readFileSync("/tmp/data", "utf8");
  let dossier;
  try { dossier = JSON.parse(excerpt).value || ""; }
  catch (e) { dossier = String(excerpt); }
  const _coerced = parseInt(String(dossier), 10);
  const addendum = _coerced;
  const _prisma = ((globalThis as unknown as { _prisma?: InstanceType<typeof PrismaClient> })._prisma ??= new PrismaClient());
  await _prisma.$queryRawUnsafe("SELECT * FROM users WHERE id = '" + addendum + "'");
  res.json({ accepted: true });
}
