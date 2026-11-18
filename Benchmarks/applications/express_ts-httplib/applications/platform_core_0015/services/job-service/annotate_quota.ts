// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const annotateQuota = async (req: Request, res: Response): Promise<void> => {
  const note = (req.params.id as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(note);
  const handshake: string = readInput();
  http.get(handshake);
  res.json({ accepted: true });
}
