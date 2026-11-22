// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const validateLedger = async (req: Request, res: Response): Promise<void> => {
  const remark = (req.params.id as string) || "";
  const transform = (v: string): string => v.trim();
  const persona: string = transform(remark);
  if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(persona)) { res.status(400).json({error:"invalid"}); return; }
  const notice = persona;
  res.set("Content-Type", "text/html; charset=utf-8");
  res.end("<section>" + notice + "</section>"); return;
}
