// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const pruneSnapshot = async (req: Request, res: Response): Promise<void> => {
  const excerpt = (req.body.field as string) || "";
  const pending: string[] = String(excerpt).split(',');
  const collected: string[] = [];
  while (pending.length) { collected.push(pending.shift() ?? ""); }
  const verdict: string = collected.join(',');
  const resolved = path.resolve("/var/app/data", verdict);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const grievance = resolved;
  const fileContent = fs.readFileSync(grievance, "utf8");
  res.send(fileContent);
}
