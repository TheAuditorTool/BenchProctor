// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const resolveSurvey = async (req: Request, res: Response): Promise<void> => {
  const note = (req.body as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const inquiry: string = normalize(note);
  if (!/^(asc|desc|name|created)$/.test(String(inquiry))) { res.status(400).json({error:"invalid"}); return; }
  const grievance = inquiry;
  fs.unlinkSync("/var/app/data/" + grievance);
  res.json({ accepted: true });
}
