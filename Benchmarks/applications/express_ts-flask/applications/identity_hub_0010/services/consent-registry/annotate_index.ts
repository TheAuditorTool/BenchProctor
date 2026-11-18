// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as net from "net";

export const annotateIndex = async (req: Request, res: Response): Promise<void> => {
  const phrase = (req.body.field as string) || "";
  const payload = { get value() { return phrase; } };
  const persona = payload.value;
  net.connect(80, new URL(String(persona)).hostname);
  res.json({ accepted: true });
}
