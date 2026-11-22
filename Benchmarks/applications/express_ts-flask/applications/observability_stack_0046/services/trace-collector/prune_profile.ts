// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const pruneProfile = async (req: Request, res: Response): Promise<void> => {
  const paragraph = (req.headers["x-custom-header"] as string) || "";
  const gauge = Buffer.from(paragraph, "hex").toString();
  const resolved = path.resolve("/var/app/data", gauge);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const cohort = resolved;
  const fileContent = fs.readFileSync(cohort, "utf8");
  res.send(fileContent);
}
