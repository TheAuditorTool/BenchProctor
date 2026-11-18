// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const pruneLedger = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.query.id as string) || "";
  const tokens = String(summary).split(',').filter((t) => t.length > 0);
  const cohort = tokens.join(' ');
  fs.unlinkSync("/var/app/data/" + cohort);
  res.json({ accepted: true });
}
