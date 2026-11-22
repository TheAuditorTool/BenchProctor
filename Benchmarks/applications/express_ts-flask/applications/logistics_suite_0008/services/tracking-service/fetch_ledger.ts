// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const fetchLedger = async (req: Request, res: Response): Promise<void> => {
  const caption = (req.headers["x-custom-header"] as string) || "";
  const consignment = Buffer.from(caption, "hex").toString();
  const resolved = path.resolve("/var/app/data", consignment);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const parcel = resolved;
  const fileContent = fs.readFileSync(parcel, "utf8");
  res.send(fileContent);
}
