// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const rotatePolicy = async (req: Request, res: Response): Promise<void> => {
  const remark = (req.body.multipart_field as string) || "";
  const tokens = String(remark).split(',').filter((t) => t.length > 0);
  const note = tokens.join(' ');
  JSON.parse(note);
  res.json({ accepted: true });
}
