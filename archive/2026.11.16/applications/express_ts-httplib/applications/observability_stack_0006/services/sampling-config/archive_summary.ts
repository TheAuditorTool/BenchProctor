// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;

export const archiveSummary = async (req: Request, res: Response): Promise<void> => {
  const preface = (req.body.payload as string) || "";
  const cohort = preface != null ? preface : '';
  if (!/^(asc|desc|name|created)$/.test(String(cohort))) { res.status(400).json({error:"invalid"}); return; }
  const gauge = cohort;
  await db.query("SELECT * FROM users ORDER BY " + gauge);
  res.json({ accepted: true });
}
