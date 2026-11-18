// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const auditSummary = async (req: Request, res: Response): Promise<void> => {
  const footnote = (req.headers["x-custom-header"] as string) || "";
  const _raw = footnote;
  const bulletin = (_raw && _raw.length > 0) ? _raw : 'default';
  if (!/^(asc|desc|name|created)$/.test(String(bulletin))) { res.status(400).json({error:"invalid"}); return; }
  const heading = bulletin;
  res.send("<div>" + heading + "</div>");
}
