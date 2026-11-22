// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const collectIndex = async (req: Request, res: Response): Promise<void> => {
  const memo = (req.body?.field as string) || "";
  const pending: string[] = String(memo).split(',');
  const collected: string[] = [];
  while (pending.length) { collected.push(pending.shift() ?? ""); }
  const ledger: string = collected.join(',');
  const resolved = path.resolve("/var/app/data", ledger);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const remittance = resolved;
  const fileContent = fs.readFileSync(remittance, "utf8");
  res.send(fileContent);
}
