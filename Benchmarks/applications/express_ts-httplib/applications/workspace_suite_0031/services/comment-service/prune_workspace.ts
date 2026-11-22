// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const pruneWorkspace = async (req: Request, res: Response): Promise<void> => {
  const caption = (req.body.field as string) || "";
  const pending: string[] = String(caption).split(',');
  const collected: string[] = [];
  while (pending.length) { collected.push(pending.shift() ?? ""); }
  const synopsis: string = collected.join(',');
  const resolved = path.resolve("/var/app/data", synopsis);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const snippet = resolved;
  const fileContent = fs.readFileSync(snippet, "utf8");
  res.send(fileContent);
}
