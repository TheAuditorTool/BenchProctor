// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as net from "net";

export const compactBundle = async (req: Request, res: Response): Promise<void> => {
  const caption = (req.headers.host as string) || "";
  const [parcel] = String(caption).split(',');
  net.connect(80, new URL(String(parcel)).hostname);
  res.json({ accepted: true });
}
