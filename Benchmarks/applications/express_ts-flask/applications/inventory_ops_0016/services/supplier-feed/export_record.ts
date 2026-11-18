// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as net from "net";

export const exportRecord = async (req: Request, res: Response): Promise<void> => {
  const citation = (req.headers.host as string) || "";
  const [backorder] = String(citation).split(',');
  net.connect(80, new URL(String(backorder)).hostname);
  res.json({ accepted: true });
}
