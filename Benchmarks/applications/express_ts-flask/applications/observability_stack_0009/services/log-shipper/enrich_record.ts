// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const enrichRecord = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.body as string) || "";
  const pending: string[] = String(summary).split(',');
  const collected: string[] = [];
  while (pending.length) { collected.push(pending.shift() ?? ""); }
  const gauge: string = collected.join(',');
  const resolved = path.resolve("/var/app/data", gauge);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const cohort = resolved;
  const fileContent = fs.readFileSync(cohort, "utf8");
  res.send(fileContent);
}
