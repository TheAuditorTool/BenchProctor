// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const annotateWindow = async (req: Request, res: Response): Promise<void> => {
  const subtitle = (req.body as string) || "";
  const transform = (v: string): string => v.trim();
  const persona: string = transform(subtitle);
  JSON.parse(persona);
  res.json({ accepted: true });
}
