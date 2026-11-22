// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const enrichThreshold = async (req: Request, res: Response): Promise<void> => {
  const snippet = (req.params.id as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(snippet);
  const montage: string = readInput();
  http.get(montage);
  res.json({ accepted: true });
}
