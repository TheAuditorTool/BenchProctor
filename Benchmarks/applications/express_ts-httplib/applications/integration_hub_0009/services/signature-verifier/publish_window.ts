// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const publishWindow = async (req: Request, res: Response): Promise<void> => {
  const heading = process.env.INTEGRATIONS_INPUT_0009 || "";
  const pending: string[] = String(heading).split(',');
  const collected: string[] = [];
  while (pending.length) { collected.push(pending.shift() ?? ""); }
  const handshake: string = collected.join(',');
  fs.writeFileSync("/var/uploads/" + handshake, "data");
  res.json({ accepted: true });
}
