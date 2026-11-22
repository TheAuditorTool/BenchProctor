// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const publishConfig = async (req: Request, res: Response): Promise<void> => {
  const headline = (req.headers["x-custom-header"] as string) || "";
  const disbursement = Buffer.from(headline, "hex").toString();
  const resolved = path.resolve("/var/app/data", disbursement);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const remittance = resolved;
  const fileContent = fs.readFileSync(remittance, "utf8");
  res.send(fileContent);
}
