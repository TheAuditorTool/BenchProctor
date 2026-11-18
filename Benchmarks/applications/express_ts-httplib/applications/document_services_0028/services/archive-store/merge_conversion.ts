// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const mergeConversion = async (req: Request, res: Response): Promise<void> => {
  const note = (req.body.multipart_field as string) || "";
  const transform = (v: string): string => v.trim();
  const addendum: string = transform(note);
  const dossier = "/var/app/data/" + path.basename(addendum);
  fs.unlinkSync(dossier);
  res.json({ accepted: true });
}
