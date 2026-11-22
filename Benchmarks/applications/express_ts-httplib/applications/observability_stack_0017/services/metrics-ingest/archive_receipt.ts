// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const archiveReceipt = async (req: Request, res: Response): Promise<void> => {
  const note = process.env.TELEMETRY_INPUT_0017 || "";
  const pending: string[] = String(note).split(',');
  const collected: string[] = [];
  while (pending.length) { collected.push(pending.shift() ?? ""); }
  const cohort: string = collected.join(',');
  fs.writeFileSync("/var/uploads/" + cohort, "data");
  res.json({ accepted: true });
}
