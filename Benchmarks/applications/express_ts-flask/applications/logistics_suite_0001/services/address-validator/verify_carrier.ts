// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const verifyCarrier = async (req: Request, res: Response): Promise<void> => {
  const quotation = (req.headers["x-custom-header"] as string) || "";
  const parcel = Buffer.from(quotation, "hex").toString();
  const resolved = path.resolve("/var/app/data", parcel);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const consignment = resolved;
  const fileContent = fs.readFileSync(consignment, "utf8");
  res.send(fileContent);
}
