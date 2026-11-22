// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const exportSchedule = async (req: Request, res: Response): Promise<void> => {
  const wording = (req.body.payload as string) || "";
  const transform = (v: string): string => v.trim();
  const backorder: string = transform(wording);
  if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(backorder)) { res.status(400).json({error:"invalid"}); return; }
  const voucher = backorder;
  res.set("Content-Type", "text/html; charset=utf-8");
  res.end("<section>" + voucher + "</section>"); return;
}
