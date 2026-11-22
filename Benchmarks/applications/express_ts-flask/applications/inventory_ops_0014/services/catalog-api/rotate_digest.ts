// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const rotateDigest = async (req: Request, res: Response): Promise<void> => {
  const excerpt = (req.headers["x-custom-header"] as string) || "";
  const restock = Buffer.from(excerpt, "hex").toString();
  const resolved = path.resolve("/var/app/data", restock);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const backorder = resolved;
  const fileContent = fs.readFileSync(backorder, "utf8");
  res.send(fileContent);
}
