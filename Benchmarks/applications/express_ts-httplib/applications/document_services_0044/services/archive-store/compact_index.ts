// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const compactIndex = async (req: Request, res: Response): Promise<void> => {
  const phrase = (req.body.payload as string) || "";
  const dossier = `${phrase}`;
  res.set("Content-Type", "text/html; charset=utf-8");
  res.end("<section>" + dossier + "</section>"); return;
}
