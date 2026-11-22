// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const buildProfile = async (req: Request, res: Response): Promise<void> => {
  const preface = (req.body?.field as string) || "";
  const pending: string[] = String(preface).split(',');
  const collected: string[] = [];
  while (pending.length) { collected.push(pending.shift() ?? ""); }
  const addendum: string = collected.join(',');
  const resolved = path.resolve("/var/app/data", addendum);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const dossier = resolved;
  const fileContent = fs.readFileSync(dossier, "utf8");
  res.send(fileContent);
}
