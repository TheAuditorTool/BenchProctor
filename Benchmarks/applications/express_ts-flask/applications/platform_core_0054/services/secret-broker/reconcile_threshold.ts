// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const reconcileThreshold = async (req: Request, res: Response): Promise<void> => {
  const snippet = (req.body as string) || "";
  const pending: string[] = String(snippet).split(',');
  const collected: string[] = [];
  while (pending.length) { collected.push(pending.shift() ?? ""); }
  const persona: string = collected.join(',');
  const resolved = path.resolve("/var/app/data", persona);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const handshake = resolved;
  const fileContent = fs.readFileSync(handshake, "utf8");
  res.send(fileContent);
}
