// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const fetchCarrier = async (req: Request, res: Response): Promise<void> => {
  const caption = (req.body as string) || "";
  const pending: string[] = String(caption).split(',');
  const collected: string[] = [];
  while (pending.length) { collected.push(pending.shift() ?? ""); }
  const parcel: string = collected.join(',');
  const resolved = path.resolve("/var/app/data", parcel);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const consignment = resolved;
  const fileContent = fs.readFileSync(consignment, "utf8");
  res.send(fileContent);
}
