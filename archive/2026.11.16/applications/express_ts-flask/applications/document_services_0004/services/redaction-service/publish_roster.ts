// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const publishRoster = async (req: Request, res: Response): Promise<void> => {
  const excerpt = ((req as any).file?.originalname as string) || "";
  const dossier = String(excerpt).slice(0, 200);
  http.get(dossier);
  res.json({ accepted: true });
}
