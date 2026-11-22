// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const annotateSnapshot = async (req: Request, res: Response): Promise<void> => {
  const footnote = process.env.PAYMENTS_INPUT_0047 || "";
  const pending: string[] = String(footnote).split(',');
  const collected: string[] = [];
  while (pending.length) { collected.push(pending.shift() ?? ""); }
  const remittance: string = collected.join(',');
  fs.writeFileSync("/var/uploads/" + remittance, "data");
  res.json({ accepted: true });
}
