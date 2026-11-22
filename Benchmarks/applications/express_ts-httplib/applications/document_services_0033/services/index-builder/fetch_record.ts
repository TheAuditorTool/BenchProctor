// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const fetchRecord = async (req: Request, res: Response): Promise<void> => {
  const snippet = (req.body as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const addendum: string = normalize(snippet);
  if (!/^(asc|desc|name|created)$/.test(String(addendum))) { res.status(400).json({error:"invalid"}); return; }
  const dossier = addendum;
  res.set("Content-Type", "text/html; charset=utf-8");
  res.end("<section>" + dossier + "</section>"); return;
}
