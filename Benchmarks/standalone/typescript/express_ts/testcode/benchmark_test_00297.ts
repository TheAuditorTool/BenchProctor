// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as nodeSerialize from "node-serialize";

export const BenchmarkTest00297 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.params.id as string) || "";
  nodeSerialize.unserialize(userInput);
  res.json({ accepted: true });
}
