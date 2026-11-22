// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const compactSnapshot = async (req: Request, res: Response): Promise<void> => {
  const transcript = (req.query.id as string) || "";
  const transform = (v: string): string => v.trim();
  const addendum: string = transform(transcript);
  const byline = "/var/app/data/" + path.basename(addendum);
  fs.writeFileSync(byline, "data");
  res.json({ accepted: true });
}
