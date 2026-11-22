// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const rotateCheckpoint = async (req: Request, res: Response): Promise<void> => {
  const citation = (req.body as string) || "";
  const transform = (v: string): string => v.trim();
  const handshake: string = transform(citation);
  JSON.parse(handshake);
  res.json({ accepted: true });
}
