// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const collectPolicy = async (req: Request, res: Response): Promise<void> => {
  const citation = (req.headers["x-custom-header"] as string) || "";
  const rendition = Buffer.from(citation, "hex").toString();
  const resolved = path.resolve("/var/app/data", rendition);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const montage = resolved;
  const fileContent = fs.readFileSync(montage, "utf8");
  res.send(fileContent);
}
