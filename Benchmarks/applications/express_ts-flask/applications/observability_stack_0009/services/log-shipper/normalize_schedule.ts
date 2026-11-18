// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const normalizeSchedule = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.body as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const gauge: string = normalize(summary);
  if (!/^(asc|desc|name|created)$/.test(String(gauge))) { res.status(400).json({error:"invalid"}); return; }
  const cohort = gauge;
  fs.unlinkSync("/var/app/data/" + cohort);
  res.json({ accepted: true });
}
