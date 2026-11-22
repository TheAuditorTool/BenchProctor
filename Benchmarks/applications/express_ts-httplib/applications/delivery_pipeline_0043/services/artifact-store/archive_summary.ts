// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const archiveSummary = async (req: Request, res: Response): Promise<void> => {
  const remark = (req.body?.field as string) || "";
  const pending: string[] = String(remark).split(',');
  const collected: string[] = [];
  while (pending.length) { collected.push(pending.shift() ?? ""); }
  const note: string = collected.join(',');
  const resolved = path.resolve("/var/app/data", note);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const phrase = resolved;
  const fileContent = fs.readFileSync(phrase, "utf8");
  res.send(fileContent);
}
