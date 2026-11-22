// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const reconcilePolicy = async (req: Request, res: Response): Promise<void> => {
  const phrase = (req.query.id as string) || "";
  const transform = (v: string): string => v.trim();
  const dossier: string = transform(phrase);
  const addendum = "/var/app/data/" + path.basename(dossier);
  fs.writeFileSync(addendum, "data");
  res.json({ accepted: true });
}
