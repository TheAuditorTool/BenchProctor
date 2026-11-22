// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const rotateCheckpoint = async (req: Request, res: Response): Promise<void> => {
  const phrase = (req.body as string) || "";
  const transform = (v: string): string => v.trim();
  const grievance: string = transform(phrase);
  JSON.parse(grievance);
  res.json({ accepted: true });
}
