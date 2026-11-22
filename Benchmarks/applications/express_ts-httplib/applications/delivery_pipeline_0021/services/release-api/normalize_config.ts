// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const normalizeConfig = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.body as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const phrase: string = normalize(summary);
  if (!/^(asc|desc|name|created)$/.test(String(phrase))) { res.status(400).json({error:"invalid"}); return; }
  const subtitle = phrase;
  res.set("Content-Type", "text/html; charset=utf-8");
  res.end("<section>" + subtitle + "</section>"); return;
}
