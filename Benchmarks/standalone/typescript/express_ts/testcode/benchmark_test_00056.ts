// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
import * as nodeSerialize from "node-serialize";

export const BenchmarkTest00056 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (await shared.mq.receive("app-events"));
  const data = String(userInput).replace(/\u0000/g, "");
  nodeSerialize.unserialize(data);
  res.json({ accepted: true });
}
