// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const validateSummary = async (req: Request, res: Response): Promise<void> => {
  const transcript = (req.body.multipart_field as string) || "";
  const tokens = String(transcript).split(',').filter((t) => t.length > 0);
  const consignment = tokens.join(' ');
  JSON.parse(consignment);
  res.json({ accepted: true });
}
