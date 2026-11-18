// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const publishSchedule = async (req: Request, res: Response): Promise<void> => {
  const heading = ((req as any).file?.originalname as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const voucher: string = normalize(heading);
  const resolved = path.resolve("/var/app/data", voucher);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const backorder = resolved;
  fs.writeFileSync(backorder, "data");
  res.json({ accepted: true });
}
