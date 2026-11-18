// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const verifySchedule = async (req: Request, res: Response): Promise<void> => {
  const paragraph = (req.query.id as string) || "";
  const tokens = String(paragraph).split(',').filter((t) => t.length > 0);
  const bulletin = tokens.join(' ');
  fs.unlinkSync("/var/app/data/" + bulletin);
  res.json({ accepted: true });
}
