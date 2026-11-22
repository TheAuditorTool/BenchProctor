// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const resolveWindow = async (req: Request, res: Response): Promise<void> => {
  const note = (req.body?.field as string) || "";
  const pending: string[] = String(note).split(',');
  const collected: string[] = [];
  while (pending.length) { collected.push(pending.shift() ?? ""); }
  const cohort: string = collected.join(',');
  const resolved = path.resolve("/var/app/data", cohort);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const gauge = resolved;
  const fileContent = fs.readFileSync(gauge, "utf8");
  res.send(fileContent);
}
