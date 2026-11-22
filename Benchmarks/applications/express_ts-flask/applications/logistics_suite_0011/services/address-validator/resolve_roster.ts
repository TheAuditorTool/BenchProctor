// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const resolveRoster = async (req: Request, res: Response): Promise<void> => {
  const citation = (req.body?.field as string) || "";
  const pending: string[] = String(citation).split(',');
  const collected: string[] = [];
  while (pending.length) { collected.push(pending.shift() ?? ""); }
  const consignment: string = collected.join(',');
  fs.writeFileSync("/var/uploads/" + consignment, "data");
  res.json({ accepted: true });
}
