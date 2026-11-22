// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const formatHeader = async (req: Request, res: Response): Promise<void> => {
  const notice = (req.headers["x-custom-header"] as string) || "";
  const backorder = Buffer.from(notice, "hex").toString();
  const resolved = path.resolve("/var/app/data", backorder);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const voucher = resolved;
  const fileContent = fs.readFileSync(voucher, "utf8");
  res.send(fileContent);
}
