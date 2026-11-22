// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const archiveBundle = async (req: Request, res: Response): Promise<void> => {
  const wording = (req.query.id as string) || "";
  const transform = (v: string): string => v.trim();
  const addendum: string = transform(wording);
  const dossier = "/var/app/data/" + path.basename(addendum);
  fs.writeFileSync(dossier, "data");
  res.json({ accepted: true });
}
