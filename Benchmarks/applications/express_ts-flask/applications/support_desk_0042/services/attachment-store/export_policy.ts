// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const exportPolicy = async (req: Request, res: Response): Promise<void> => {
  const blurb = (req.params.id as string) || "";
  const transform = (v: string): string => v.trim();
  const inquiry: string = transform(blurb);
  if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(inquiry)) { res.status(400).json({error:"invalid"}); return; }
  const grievance = inquiry;
  res.set("Content-Type", "text/html; charset=utf-8");
  res.end("<section>" + grievance + "</section>"); return;
}
