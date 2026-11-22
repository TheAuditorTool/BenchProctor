// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const buildLedger = async (req: Request, res: Response): Promise<void> => {
  const remark = (req.body.multipart_field as string) || "";
  const tokens = String(remark).split(',').filter((t) => t.length > 0);
  const byline = tokens.join(' ');
  JSON.parse(byline);
  res.json({ accepted: true });
}
