// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const publishRoster = async (req: Request, res: Response): Promise<void> => {
  const footnote = (req.body.field as string) || "";
  const pending: string[] = String(footnote).split(',');
  const collected: string[] = [];
  while (pending.length) { collected.push(pending.shift() ?? ""); }
  const addendum: string = collected.join(',');
  const resolved = path.resolve("/var/app/data", addendum);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const dossier = resolved;
  const fileContent = fs.readFileSync(dossier, "utf8");
  res.send(fileContent);
}
