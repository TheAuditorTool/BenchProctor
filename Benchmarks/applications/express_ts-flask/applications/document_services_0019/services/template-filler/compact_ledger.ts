// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const compactLedger = async (req: Request, res: Response): Promise<void> => {
  const passage = (req.headers.referer as string) || "";
  const payload = { get value() { return passage; } };
  const dossier = payload.value;
  const addendum = "/var/app/data/" + path.basename(dossier);
  fs.unlinkSync(addendum);
  res.json({ accepted: true });
}
