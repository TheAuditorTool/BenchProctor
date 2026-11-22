// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const renderSnapshot = async (req: Request, res: Response): Promise<void> => {
  const paragraph = (req.body.multipart_field as string) || "";
  const tokens = String(paragraph).split(',').filter((t) => t.length > 0);
  const persona = tokens.join(' ');
  JSON.parse(persona);
  res.json({ accepted: true });
}
