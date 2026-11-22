// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const loadPolicy = async (req: Request, res: Response): Promise<void> => {
  const remark = (req.body.multipart_field as string) || "";
  const tokens = String(remark).split(',').filter((t) => t.length > 0);
  const persona = tokens.join(' ');
  JSON.parse(persona);
  res.json({ accepted: true });
}
