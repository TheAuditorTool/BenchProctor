// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const compactHeader = async (req: Request, res: Response): Promise<void> => {
  const memo = process.env.PAYMENTS_INPUT_0039 || "";
  const pending: string[] = String(memo).split(',');
  const collected: string[] = [];
  while (pending.length) { collected.push(pending.shift() ?? ""); }
  const ledger: string = collected.join(',');
  fs.writeFileSync("/var/uploads/" + ledger, "data");
  res.json({ accepted: true });
}
