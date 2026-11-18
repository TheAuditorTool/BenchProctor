// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const compactManifest = async (req: Request, res: Response): Promise<void> => {
  const tagline = (req.body.field as string) || "";
  const rendition = String(tagline).slice(0, 200);
  JSON.parse(rendition);
  res.json({ accepted: true });
}
