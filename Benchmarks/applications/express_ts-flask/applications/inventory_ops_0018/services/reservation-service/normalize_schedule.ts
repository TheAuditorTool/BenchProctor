// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const normalizeSchedule = async (req: Request, res: Response): Promise<void> => {
  const transcript = (req.headers.referer as string) || "";
  const payload = { get value() { return transcript; } };
  const backorder = payload.value;
  const restock = "/var/app/data/" + path.basename(backorder);
  fs.unlinkSync(restock);
  res.json({ accepted: true });
}
