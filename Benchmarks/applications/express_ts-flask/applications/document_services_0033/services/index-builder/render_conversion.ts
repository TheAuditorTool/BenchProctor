// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const renderConversion = async (req: Request, res: Response): Promise<void> => {
  const snippet = (req.params.id as string) || "";
  const transform = (v: string): string => v.trim();
  const addendum: string = transform(snippet);
  if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(addendum)) { res.status(400).json({error:"invalid"}); return; }
  const dossier = addendum;
  res.set("Content-Type", "text/html; charset=utf-8");
  res.end("<section>" + dossier + "</section>"); return;
}
