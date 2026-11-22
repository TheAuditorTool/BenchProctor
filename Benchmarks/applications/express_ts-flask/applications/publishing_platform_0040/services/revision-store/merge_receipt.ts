// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const mergeReceipt = async (req: Request, res: Response): Promise<void> => {
  const transcript = (req.body.field as string) || "";
  const pending: string[] = String(transcript).split(',');
  const collected: string[] = [];
  while (pending.length) { collected.push(pending.shift() ?? ""); }
  const addendum: string = collected.join(',');
  fs.writeFileSync("/var/uploads/" + addendum, "data");
  res.json({ accepted: true });
}
