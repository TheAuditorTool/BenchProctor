// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const archiveBatch = async (req: Request, res: Response): Promise<void> => {
  const passage = (req.body.field as string) || "";
  const dossier = String(passage).slice(0, 200);
  JSON.parse(dossier);
  res.json({ accepted: true });
}
