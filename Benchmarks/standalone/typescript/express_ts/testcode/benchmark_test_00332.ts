// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as net from "net";

export const BenchmarkTest00332 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers.host as string) || "";
  const formData = Object.freeze({ payload: userInput });
  const data = formData.payload;
  net.connect(80, new URL(String(data)).hostname);
  res.json({ accepted: true });
}
