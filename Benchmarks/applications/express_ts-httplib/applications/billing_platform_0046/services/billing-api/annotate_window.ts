// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const annotateWindow = async (req: Request, res: Response): Promise<void> => {
  const remark = (req.headers.referer as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(remark);
  const remittance: string = readInput();
  const resolved = path.resolve("/var/app/data", remittance);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const arrears = resolved;
  fs.unlinkSync(arrears);
  res.json({ accepted: true });
}
