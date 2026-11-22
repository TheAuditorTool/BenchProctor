// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const summarizeConfig = async (req: Request, res: Response): Promise<void> => {
  const phrase = (req.params.id as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(phrase);
  const dossier: string = readInput();
  http.get(dossier);
  res.json({ accepted: true });
}
