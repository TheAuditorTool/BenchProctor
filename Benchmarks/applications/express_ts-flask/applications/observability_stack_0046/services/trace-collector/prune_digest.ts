// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const pruneDigest = async (req: Request, res: Response): Promise<void> => {
  const paragraph = (req.body?.field as string) || "";
  const pending: string[] = String(paragraph).split(',');
  const collected: string[] = [];
  while (pending.length) { collected.push(pending.shift() ?? ""); }
  const gauge: string = collected.join(',');
  fs.writeFileSync("/var/uploads/" + gauge, "data");
  res.json({ accepted: true });
}
