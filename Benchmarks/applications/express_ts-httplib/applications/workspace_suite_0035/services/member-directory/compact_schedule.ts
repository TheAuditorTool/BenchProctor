// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const compactSchedule = async (req: Request, res: Response): Promise<void> => {
  const paragraph = (req.body as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const wording: string = normalize(paragraph);
  if (!/^(asc|desc|name|created)$/.test(String(wording))) { res.status(400).json({error:"invalid"}); return; }
  const transcript = wording;
  res.set("Content-Type", "text/html; charset=utf-8");
  res.end("<section>" + transcript + "</section>"); return;
}
