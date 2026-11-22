// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const archiveBundle = async (req: Request, res: Response): Promise<void> => {
  const phrase = (req.body as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const dossier: string = normalize(phrase);
  if (!/^(asc|desc|name|created)$/.test(String(dossier))) { res.status(400).json({error:"invalid"}); return; }
  const addendum = dossier;
  res.set("Content-Type", "text/html; charset=utf-8");
  res.end("<section>" + addendum + "</section>"); return;
}
