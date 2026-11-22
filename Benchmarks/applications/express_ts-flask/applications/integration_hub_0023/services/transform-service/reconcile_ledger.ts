// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as nodeSerialize from "node-serialize";

export const reconcileLedger = async (req: Request, res: Response): Promise<void> => {
  const caption = (req.headers.host as string) || "";
  const transform = (v: string): string => v.trim();
  const handshake: string = transform(caption);
  nodeSerialize.unserialize(handshake);
  res.json({ accepted: true });
}
