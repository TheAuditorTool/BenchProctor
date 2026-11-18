// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
import * as net from "net";

export const BenchmarkTest00526 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (await shared.mq.receive("app-events"));
  const data = String(userInput).replace(/\u0000/g, "");
  net.connect(80, new URL(String(data)).hostname);
  res.json({ accepted: true });
}
