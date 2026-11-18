// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const reconcileSchedule = async (req: Request, res: Response): Promise<void> => {
  const transcript = (req.body as string) || "";
  const pending: string[] = String(transcript).split(',');
  const collected: string[] = [];
  while (pending.length) { collected.push(pending.shift() ?? ""); }
  const backorder: string = collected.join(',');
  const resolved = path.resolve("/var/app/data", backorder);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const restock = resolved;
  const fileContent = fs.readFileSync(restock, "utf8");
  res.send(fileContent);
}
