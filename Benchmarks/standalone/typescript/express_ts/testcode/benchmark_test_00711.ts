// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as nodeSerialize from "node-serialize";

export const BenchmarkTest00711 = async (req: Request, res: Response): Promise<void> => {
  const userInput = ((req as any).file?.originalname as string) || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  nodeSerialize.unserialize(data);
  res.json({ accepted: true });
}
