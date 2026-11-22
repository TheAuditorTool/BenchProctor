// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const exportDigest = async (req: Request, res: Response): Promise<void> => {
  const wording = (req.headers.host as string) || "";
  const transform = (v: string): string => v.trim();
  const backorder: string = transform(wording);
  if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(backorder)) { res.status(400).json({error:"invalid"}); return; }
  const voucher = backorder;
  const fileContent = fs.readFileSync("/var/app/data/" + voucher, "utf8");
  res.send(fileContent);
}
