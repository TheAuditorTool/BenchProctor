// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const annotateManifest = async (req: Request, res: Response): Promise<void> => {
  const caption = (req.headers.referer as string) || "";
  const payload = { get value() { return caption; } };
  const ledger = payload.value;
  const remittance = "/var/app/data/" + path.basename(ledger);
  fs.unlinkSync(remittance);
  res.json({ accepted: true });
}
