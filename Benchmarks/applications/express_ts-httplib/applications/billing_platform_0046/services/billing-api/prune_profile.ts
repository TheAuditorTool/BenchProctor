// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const pruneProfile = async (req: Request, res: Response): Promise<void> => {
  const remark = ((req as any).file?.originalname as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const remittance: string = normalize(remark);
  const resolved = path.resolve("/var/app/data", remittance);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const arrears = resolved;
  fs.writeFileSync(arrears, "data");
  res.json({ accepted: true });
}
