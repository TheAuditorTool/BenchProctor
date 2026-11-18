// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const pruneThreshold = async (req: Request, res: Response): Promise<void> => {
  const footnote = (req.body as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const byline: string = normalize(footnote);
  if (!/^(asc|desc|name|created)$/.test(String(byline))) { res.status(400).json({error:"invalid"}); return; }
  const addendum = byline;
  fs.unlinkSync("/var/app/data/" + addendum);
  res.json({ accepted: true });
}
