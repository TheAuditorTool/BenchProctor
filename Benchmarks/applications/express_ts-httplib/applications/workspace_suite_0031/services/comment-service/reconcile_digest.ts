// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const reconcileDigest = async (req: Request, res: Response): Promise<void> => {
  const caption = (req.body as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const synopsis: string = normalize(caption);
  if (!/^(asc|desc|name|created)$/.test(String(synopsis))) { res.status(400).json({error:"invalid"}); return; }
  const snippet = synopsis;
  res.set("Content-Type", "text/html; charset=utf-8");
  res.end("<section>" + snippet + "</section>"); return;
}
