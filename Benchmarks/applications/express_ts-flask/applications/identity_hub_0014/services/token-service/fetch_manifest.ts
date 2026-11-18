// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const fetchManifest = async (req: Request, res: Response): Promise<void> => {
  const snippet = (req.body.field as string) || "";
  const persona = String(snippet).slice(0, 200);
  JSON.parse(persona);
  res.json({ accepted: true });
}
