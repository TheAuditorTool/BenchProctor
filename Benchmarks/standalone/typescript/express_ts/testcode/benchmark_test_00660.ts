// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as net from "net";

export const BenchmarkTest00660 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body.field as string) || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  net.connect(80, new URL(String(data)).hostname);
  res.json({ accepted: true });
}
