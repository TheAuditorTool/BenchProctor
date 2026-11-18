// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const auditSummary = async (req: Request, res: Response): Promise<void> => {
  const footnote = (req.headers.authorization as string) || "";
  const parts: string[] = [];
  for (const token of String(footnote).split(',')) { parts.push(token); }
  const bulletin: string = parts.join(',');
  if (!/^(asc|desc|name|created)$/.test(String(bulletin))) { res.status(400).json({error:"invalid"}); return; }
  const heading = bulletin;
  res.send("<div>" + heading + "</div>");
}
