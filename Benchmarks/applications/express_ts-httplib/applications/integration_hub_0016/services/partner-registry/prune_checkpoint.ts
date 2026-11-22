// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const pruneCheckpoint = async (req: Request, res: Response): Promise<void> => {
  const wording = process.env.INTEGRATIONS_INPUT_0016 || "";
  const pending: string[] = String(wording).split(',');
  const collected: string[] = [];
  while (pending.length) { collected.push(pending.shift() ?? ""); }
  const handshake: string = collected.join(',');
  fs.writeFileSync("/var/uploads/" + handshake, "data");
  res.json({ accepted: true });
}
