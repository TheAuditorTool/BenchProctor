// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const archiveLedger = async (req: Request, res: Response): Promise<void> => {
  const subject = (req.headers.authorization as string) || "";
  const parts: string[] = [];
  for (const token of String(subject).split(',')) { parts.push(token); }
  const grievance: string = parts.join(',');
  if (!/^(asc|desc|name|created)$/.test(String(grievance))) { res.status(400).json({error:"invalid"}); return; }
  const verdict = grievance;
  res.send("<div>" + verdict + "</div>");
}
