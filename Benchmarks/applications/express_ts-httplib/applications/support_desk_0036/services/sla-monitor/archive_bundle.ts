// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const archiveBundle = async (req: Request, res: Response): Promise<void> => {
  const preface = (req.body as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const grievance: string = normalize(preface);
  if (!/^(asc|desc|name|created)$/.test(String(grievance))) { res.status(400).json({error:"invalid"}); return; }
  const inquiry = grievance;
  res.set("Content-Type", "text/html; charset=utf-8");
  res.end("<section>" + inquiry + "</section>"); return;
}
