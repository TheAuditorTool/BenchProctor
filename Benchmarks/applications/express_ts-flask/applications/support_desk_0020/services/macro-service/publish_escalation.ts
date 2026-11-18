// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as net from "net";

export const publishEscalation = async (req: Request, res: Response): Promise<void> => {
  const phrase = (req.headers.host as string) || "";
  const [inquiry] = String(phrase).split(',');
  net.connect(80, new URL(String(inquiry)).hostname);
  res.json({ accepted: true });
}
