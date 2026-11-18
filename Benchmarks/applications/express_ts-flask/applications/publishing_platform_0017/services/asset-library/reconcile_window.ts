// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const reconcileWindow = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.headers.referer as string) || "";
  const payload = { get value() { return summary; } };
  const addendum = payload.value;
  const byline = "/var/app/data/" + path.basename(addendum);
  fs.unlinkSync(byline);
  res.json({ accepted: true });
}
