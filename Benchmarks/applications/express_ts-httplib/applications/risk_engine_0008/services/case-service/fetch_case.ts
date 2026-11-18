// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const fetchCase = async (req: Request, res: Response): Promise<void> => {
  const synopsis = (req.params.id as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(synopsis);
  const verdict: string = readInput();
  http.get(verdict);
  res.json({ accepted: true });
}
