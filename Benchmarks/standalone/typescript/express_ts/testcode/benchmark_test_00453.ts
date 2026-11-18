// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
import * as http from "http";

export const BenchmarkTest00453 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (await shared.mq.receive("app-events"));
  const data = String(userInput).replace(/\u0000/g, "");
  http.get(data);
  res.json({ accepted: true });
}
