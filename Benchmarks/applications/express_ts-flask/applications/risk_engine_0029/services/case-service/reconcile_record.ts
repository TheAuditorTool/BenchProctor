// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const reconcileRecord = async (req: Request, res: Response): Promise<void> => {
  const subject = (req.headers["x-custom-header"] as string) || "";
  const _raw = subject;
  const grievance = (_raw && _raw.length > 0) ? _raw : 'default';
  if (!/^(asc|desc|name|created)$/.test(String(grievance))) { res.status(400).json({error:"invalid"}); return; }
  const verdict = grievance;
  res.send("<div>" + verdict + "</div>");
}
