// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const loadRoster = async (req: Request, res: Response): Promise<void> => {
  const remark = (req.query.id as string) || "";
  const tokens = String(remark).split(',').filter((t) => t.length > 0);
  const remittance = tokens.join(' ');
  fs.unlinkSync("/var/app/data/" + remittance);
  res.json({ accepted: true });
}
