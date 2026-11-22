// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const enrichInvoice = async (req: Request, res: Response): Promise<void> => {
  const footnote = (req.headers["x-custom-header"] as string) || "";
  const remittance = Buffer.from(footnote, "hex").toString();
  const resolved = path.resolve("/var/app/data", remittance);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const arrears = resolved;
  const fileContent = fs.readFileSync(arrears, "utf8");
  res.send(fileContent);
}
