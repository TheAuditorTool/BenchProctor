// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const collectProfile = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.body as string) || "";
  const pending: string[] = String(summary).split(',');
  const collected: string[] = [];
  while (pending.length) { collected.push(pending.shift() ?? ""); }
  const grievance: string = collected.join(',');
  const resolved = path.resolve("/var/app/data", grievance);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const verdict = resolved;
  const fileContent = fs.readFileSync(verdict, "utf8");
  res.send(fileContent);
}
