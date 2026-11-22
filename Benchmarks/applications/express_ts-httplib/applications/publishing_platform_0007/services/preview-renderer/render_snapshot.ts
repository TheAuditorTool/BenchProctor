// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const renderSnapshot = async (req: Request, res: Response): Promise<void> => {
  const remark = (req.body as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const byline: string = normalize(remark);
  if (!/^(asc|desc|name|created)$/.test(String(byline))) { res.status(400).json({error:"invalid"}); return; }
  const addendum = byline;
  res.set("Content-Type", "text/html; charset=utf-8");
  res.end("<section>" + addendum + "</section>"); return;
}
