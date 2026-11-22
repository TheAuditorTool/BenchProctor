// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const exportWindow = async (req: Request, res: Response): Promise<void> => {
  const footnote = (req.headers["x-custom-header"] as string) || "";
  const addendum = Buffer.from(footnote, "hex").toString();
  const resolved = path.resolve("/var/app/data", addendum);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const dossier = resolved;
  const fileContent = fs.readFileSync(dossier, "utf8");
  res.send(fileContent);
}
