// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const archiveRecord = async (req: Request, res: Response): Promise<void> => {
  const synopsis = (req.body as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const rendition: string = normalize(synopsis);
  if (!/^(asc|desc|name|created)$/.test(String(rendition))) { res.status(400).json({error:"invalid"}); return; }
  const montage = rendition;
  res.set("Content-Type", "text/html; charset=utf-8");
  res.end("<section>" + montage + "</section>"); return;
}
