// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const enrichConfig = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.body as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const addendum: string = normalize(summary);
  if (!/^(asc|desc|name|created)$/.test(String(addendum))) { res.status(400).json({error:"invalid"}); return; }
  const byline = addendum;
  fs.unlinkSync("/var/app/data/" + byline);
  res.json({ accepted: true });
}
