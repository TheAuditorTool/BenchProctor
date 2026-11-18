// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const formatDigest = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.headers.authorization as string) || "";
  const parts: string[] = [];
  for (const token of String(summary).split(',')) { parts.push(token); }
  const cohort: string = parts.join(',');
  if (!/^(asc|desc|name|created)$/.test(String(cohort))) { res.status(400).json({error:"invalid"}); return; }
  const gauge = cohort;
  res.send("<div>" + gauge + "</div>");
}
