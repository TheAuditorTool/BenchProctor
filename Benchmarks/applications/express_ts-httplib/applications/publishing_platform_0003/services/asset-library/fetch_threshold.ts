// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const fetchThreshold = async (req: Request, res: Response): Promise<void> => {
  const heading = (req.body as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const addendum: string = normalize(heading);
  if (!/^(asc|desc|name|created)$/.test(String(addendum))) { res.status(400).json({error:"invalid"}); return; }
  const byline = addendum;
  res.set("Content-Type", "text/html; charset=utf-8");
  res.end("<section>" + byline + "</section>"); return;
}
