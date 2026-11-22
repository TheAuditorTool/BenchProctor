// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const summarizeCheckpoint = async (req: Request, res: Response): Promise<void> => {
  const heading = (req.body as string) || "";
  const transform = (v: string): string => v.trim();
  const handshake: string = transform(heading);
  JSON.parse(handshake);
  res.json({ accepted: true });
}
