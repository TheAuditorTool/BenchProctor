// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const collectSummary = async (req: Request, res: Response): Promise<void> => {
  const phrase = (req.headers.authorization as string) || "";
  const tokens = String(phrase).split(',').filter((t) => t.length > 0);
  const parcel = tokens.join(' ');
  fs.unlinkSync("/var/app/data/" + parcel);
  res.json({ accepted: true });
}
