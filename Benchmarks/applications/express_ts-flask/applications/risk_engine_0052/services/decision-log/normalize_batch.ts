// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const normalizeBatch = async (req: Request, res: Response): Promise<void> => {
  const memo = (req.body?.multipart_field as string) || "";
  const tokens = String(memo).split(',').filter((t) => t.length > 0);
  const verdict = tokens.join(' ');
  JSON.parse(verdict);
  res.json({ accepted: true });
}
