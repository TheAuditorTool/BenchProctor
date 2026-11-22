// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const reconcileManifest = async (req: Request, res: Response): Promise<void> => {
  const caption = (req.params.id as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(caption);
  const synopsis: string = readInput();
  http.get(synopsis);
  res.json({ accepted: true });
}
