// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const buildSnapshot = async (req: Request, res: Response): Promise<void> => {
  const memo = (req.body?.multipart_field as string) || "";
  const tokens = String(memo).split(',').filter((t) => t.length > 0);
  const backorder = tokens.join(' ');
  JSON.parse(backorder);
  res.json({ accepted: true });
}
