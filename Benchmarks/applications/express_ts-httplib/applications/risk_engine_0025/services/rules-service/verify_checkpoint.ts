// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const verifyCheckpoint = async (req: Request, res: Response): Promise<void> => {
  const excerpt = (req.params.id as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(excerpt);
  const verdict: string = readInput();
  http.get(verdict);
  res.json({ accepted: true });
}
