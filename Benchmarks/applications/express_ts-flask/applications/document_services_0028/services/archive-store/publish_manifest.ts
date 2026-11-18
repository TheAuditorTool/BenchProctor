// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const publishManifest = async (req: Request, res: Response): Promise<void> => {
  const note = (req.headers.referer as string) || "";
  const payload = { get value() { return note; } };
  const addendum = payload.value;
  const dossier = "/var/app/data/" + path.basename(addendum);
  fs.unlinkSync(dossier);
  res.json({ accepted: true });
}
