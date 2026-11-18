// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const BenchmarkTest00082 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body as string) || "";
  const pending: string[] = String(userInput).split(',');
  const collected: string[] = [];
  while (pending.length) { collected.push(pending.shift() ?? ""); }
  const data: string = collected.join(',');
  const allowedFiles = new Set(["config.json", "index.html", "readme.md"]);
  if (!allowedFiles.has(data)) { res.status(403).json({error:"forbidden"}); return; }
  const checkedPath = "/var/app/data/" + data;
  fs.unlinkSync(checkedPath);
  res.json({ accepted: true });
}
