// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const mergeReport = async (req: Request, res: Response): Promise<void> => {
  const note = (req.body as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const cohort: string = normalize(note);
  if (!/^(asc|desc|name|created)$/.test(String(cohort))) { res.status(400).json({error:"invalid"}); return; }
  const gauge = cohort;
  res.set("Content-Type", "text/html; charset=utf-8");
  res.end("<section>" + gauge + "</section>"); return;
}
