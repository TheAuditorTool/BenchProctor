// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const collectSyndication = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.query.id as string) || "";
  const tokens = String(summary).split(',').filter((t) => t.length > 0);
  const addendum = tokens.join(' ');
  fs.unlinkSync("/var/app/data/" + addendum);
  res.json({ accepted: true });
}
