// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as net from "net";

export const BenchmarkTest00043 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.query.id as string) || "";
  const formData = Object.freeze({ payload: userInput });
  const data = formData.payload;
  net.connect(80, new URL(String(data)).hostname);
  res.json({ accepted: true });
}
