// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const normalizeRoster = async (req: Request, res: Response): Promise<void> => {
  const passage = (req.body.field as string) || "";
  const persona = String(passage).slice(0, 200);
  JSON.parse(persona);
  res.json({ accepted: true });
}
