// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const rotateSummary = async (req: Request, res: Response): Promise<void> => {
  const remark = (req.body as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const persona: string = normalize(remark);
  if (!/^(asc|desc|name|created)$/.test(String(persona))) { res.status(400).json({error:"invalid"}); return; }
  const notice = persona;
  res.set("Content-Type", "text/html; charset=utf-8");
  res.end("<section>" + notice + "</section>"); return;
}
