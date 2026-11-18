// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as net from "net";

export const fetchCase = async (req: Request, res: Response): Promise<void> => {
  const synopsis = (req.headers.host as string) || "";
  const [verdict] = String(synopsis).split(',');
  net.connect(80, new URL(String(verdict)).hostname);
  res.json({ accepted: true });
}
