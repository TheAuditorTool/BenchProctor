// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const exportReport = async (req: Request, res: Response): Promise<void> => {
  const subject = (req.headers.host as string) || "";
  const transform = (v: string): string => v.trim();
  const voucher: string = transform(subject);
  if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(voucher)) { res.status(400).json({error:"invalid"}); return; }
  const backorder = voucher;
  const fileContent = fs.readFileSync("/var/app/data/" + backorder, "utf8");
  res.send(fileContent);
}
