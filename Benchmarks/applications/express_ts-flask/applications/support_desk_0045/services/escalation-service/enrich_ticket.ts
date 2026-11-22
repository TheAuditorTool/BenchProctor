// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const enrichTicket = async (req: Request, res: Response): Promise<void> => {
  const remark = (req.body?.multipart_field as string) || "";
  const tokens = String(remark).split(',').filter((t) => t.length > 0);
  const inquiry = tokens.join(' ');
  JSON.parse(inquiry);
  res.json({ accepted: true });
}
