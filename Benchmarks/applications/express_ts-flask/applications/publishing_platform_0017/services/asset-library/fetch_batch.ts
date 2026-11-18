// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as net from "net";

export const fetchBatch = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.headers.host as string) || "";
  const [addendum] = String(summary).split(',');
  net.connect(80, new URL(String(addendum)).hostname);
  res.json({ accepted: true });
}
