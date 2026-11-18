// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const exportRecord = async (req: Request, res: Response): Promise<void> => {
  const citation = (req.headers.referer as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(citation);
  const parcel: string = readInput();
  const resolved = path.resolve("/var/app/data", parcel);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const consignment = resolved;
  fs.unlinkSync(consignment);
  res.json({ accepted: true });
}
