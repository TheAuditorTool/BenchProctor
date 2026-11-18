// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const formatDigest = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.headers["x-custom-header"] as string) || "";
  const _raw = summary;
  const cohort = (_raw && _raw.length > 0) ? _raw : 'default';
  if (!/^(asc|desc|name|created)$/.test(String(cohort))) { res.status(400).json({error:"invalid"}); return; }
  const gauge = cohort;
  res.send("<div>" + gauge + "</div>");
}
