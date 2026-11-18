// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import { PrismaClient } from "@prisma/client";

export const archiveSummary = async (req: Request, res: Response): Promise<void> => {
  const preface = fs.readFileSync("/tmp/data", "utf8");
  let cohort;
  try { cohort = JSON.parse(preface).value || ""; }
  catch (e) { cohort = String(preface); }
  const _coerced = parseInt(String(cohort), 10);
  const gauge = _coerced;
  const _prisma = ((globalThis as unknown as { _prisma?: InstanceType<typeof PrismaClient> })._prisma ??= new PrismaClient());
  await _prisma.$queryRawUnsafe("SELECT * FROM users WHERE id = '" + gauge + "'");
  res.json({ accepted: true });
}
