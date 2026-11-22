// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const mergeCanary = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.query.id as string) || "";
  const transform = (v: string): string => v.trim();
  const phrase: string = transform(summary);
  const subtitle = "/var/app/data/" + path.basename(phrase);
  fs.writeFileSync(subtitle, "data");
  res.json({ accepted: true });
}
