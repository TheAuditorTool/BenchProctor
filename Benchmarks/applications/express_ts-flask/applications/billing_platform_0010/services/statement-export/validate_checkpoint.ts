// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const validateCheckpoint = async (req: Request, res: Response): Promise<void> => {
  const headline = (req.body.multipart_field as string) || "";
  const tokens = String(headline).split(',').filter((t) => t.length > 0);
  const remittance = tokens.join(' ');
  JSON.parse(remittance);
  res.json({ accepted: true });
}
