// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const BenchmarkTest00338 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.query.id as string) || "";
  const data = userInput != null ? userInput : '';
  const allowedFiles = new Set(["config.json", "index.html", "readme.md"]);
  if (!allowedFiles.has(data)) { res.status(403).json({error:"forbidden"}); return; }
  const checkedPath = "/var/app/data/" + data;
  fs.writeFileSync(checkedPath, "data");
  res.json({ accepted: true });
}
