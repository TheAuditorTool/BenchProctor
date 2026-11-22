// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const fetchManifest = async (req: Request, res: Response): Promise<void> => {
  const phrase = (req.params.id as string) || "";
  const transform = (v: string): string => v.trim();
  const grievance: string = transform(phrase);
  if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(grievance)) { res.status(400).json({error:"invalid"}); return; }
  const inquiry = grievance;
  res.set("Content-Type", "text/html; charset=utf-8");
  res.end("<section>" + inquiry + "</section>"); return;
}
