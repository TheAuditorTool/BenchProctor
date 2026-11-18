// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const BenchmarkTest00706 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body.multipart_field as string) || "";
  const data = String(userInput).replace(/\u0000/g, "");
  const resolved = path.resolve("/var/app/data", data);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const checkedPath = resolved;
  const fileContent = fs.readFileSync(checkedPath, "utf8");
  res.send(fileContent);
}
