// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as net from "net";
import * as nodeUtil from "util";

export const BenchmarkTest00143 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.cookies?.session_token as string) || "";
  const data = nodeUtil.format("%s", userInput);
  net.connect(80, new URL(String(data)).hostname);
  res.json({ accepted: true });
}
