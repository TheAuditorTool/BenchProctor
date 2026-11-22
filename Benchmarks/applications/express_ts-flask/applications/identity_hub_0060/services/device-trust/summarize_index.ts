// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as nodeSerialize from "node-serialize";

export const summarizeIndex = async (req: Request, res: Response): Promise<void> => {
  const paragraph = (req.headers.host as string) || "";
  const transform = (v: string): string => v.trim();
  const persona: string = transform(paragraph);
  nodeSerialize.unserialize(persona);
  res.json({ accepted: true });
}
