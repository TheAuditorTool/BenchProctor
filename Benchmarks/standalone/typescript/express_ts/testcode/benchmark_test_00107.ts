// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const BenchmarkTest00107 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body as string) || "";
  const data = String(userInput).slice(0, 200);
  const allowedFiles = new Set(["config.json", "index.html", "readme.md"]);
  if (!allowedFiles.has(data)) { res.status(403).json({error:"forbidden"}); return; }
  const checkedPath = "/var/app/data/" + data;
  const fileContent = fs.readFileSync(checkedPath, "utf8");
  res.send(fileContent);
}
