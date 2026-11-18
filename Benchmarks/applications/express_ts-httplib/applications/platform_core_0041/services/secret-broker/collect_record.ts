// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const collectRecord = async (req: Request, res: Response): Promise<void> => {
  const passage = (req.params.id as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(passage);
  const persona: string = readInput();
  http.get(persona);
  res.json({ accepted: true });
}
