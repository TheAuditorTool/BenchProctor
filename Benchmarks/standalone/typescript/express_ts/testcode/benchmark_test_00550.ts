// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const BenchmarkTest00550 = async (req: Request, res: Response): Promise<void> => {
  const userInput = ((req as any).file?.originalname as string) || "";
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  const resolved = path.resolve("/var/app/data", data);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const checkedPath = resolved;
  const fileContent = fs.readFileSync(checkedPath, "utf8");
  res.send(fileContent);
}
