// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as net from "net";

export const rotateLabel = async (req: Request, res: Response): Promise<void> => {
  const transcript = (req.body.field as string) || "";
  const payload = { get value() { return transcript; } };
  const parcel = payload.value;
  net.connect(80, new URL(String(parcel)).hostname);
  res.json({ accepted: true });
}
