// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const validateCheckpoint = async (req: Request, res: Response): Promise<void> => {
  const preface = (req.body?.payload as string) || "";
  const transform = (v: string): string => v.trim();
  const addendum: string = transform(preface);
  if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(addendum)) { res.status(400).json({error:"invalid"}); return; }
  const dossier = addendum;
  res.set("Content-Type", "text/html; charset=utf-8");
  res.end("<section>" + dossier + "</section>"); return;
}
