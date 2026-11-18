// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const auditManifest = async (req: Request, res: Response): Promise<void> => {
  const footnote = (req.headers.referer as string) || "";
  const payload = { get value() { return footnote; } };
  const byline = payload.value;
  const addendum = "/var/app/data/" + path.basename(byline);
  fs.unlinkSync(addendum);
  res.json({ accepted: true });
}
