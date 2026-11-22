// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const summarizePolicy = async (req: Request, res: Response): Promise<void> => {
  const paragraph = (req.params.id as string) || "";
  const transform = (v: string): string => v.trim();
  const persona: string = transform(paragraph);
  if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(persona)) { res.status(400).json({error:"invalid"}); return; }
  const blurb = persona;
  res.set("Content-Type", "text/html; charset=utf-8");
  res.end("<section>" + blurb + "</section>"); return;
}
