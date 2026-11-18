// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as net from "net";

export const BenchmarkTest00442 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers.referer as string) || "";
  const data = `${userInput}`;
  net.connect(80, new URL(String(data)).hostname);
  res.json({ accepted: true });
}
