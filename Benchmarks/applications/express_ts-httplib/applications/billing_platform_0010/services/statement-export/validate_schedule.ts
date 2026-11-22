// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const validateSchedule = async (req: Request, res: Response): Promise<void> => {
  const headline = (req.body.field as string) || "";
  const pending: string[] = String(headline).split(',');
  const collected: string[] = [];
  while (pending.length) { collected.push(pending.shift() ?? ""); }
  const remittance: string = collected.join(',');
  const resolved = path.resolve("/var/app/data", remittance);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const dunning = resolved;
  const fileContent = fs.readFileSync(dunning, "utf8");
  res.send(fileContent);
}
