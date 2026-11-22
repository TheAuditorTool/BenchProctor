// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const buildBatch = async (req: Request, res: Response): Promise<void> => {
  const tagline = (req.body as string) || "";
  const transform = (v: string): string => v.trim();
  const persona: string = transform(tagline);
  JSON.parse(persona);
  res.json({ accepted: true });
}
