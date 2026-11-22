// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const normalizeWindow = async (req: Request, res: Response): Promise<void> => {
  const citation = (req.headers["x-custom-header"] as string) || "";
  const consignment = Buffer.from(citation, "hex").toString();
  const resolved = path.resolve("/var/app/data", consignment);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const parcel = resolved;
  const fileContent = fs.readFileSync(parcel, "utf8");
  res.send(fileContent);
}
