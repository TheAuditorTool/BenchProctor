// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";

export const BenchmarkTest00313 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (await shared.mq.receive("app-events"));
  const data = Buffer.from(userInput, "base64").toString();
  JSON.parse(data);
  res.json({ accepted: true });
}
