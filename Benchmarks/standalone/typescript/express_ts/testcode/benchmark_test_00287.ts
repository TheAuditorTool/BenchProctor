// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as nodeSerialize from "node-serialize";

export const BenchmarkTest00287 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.params.id as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(userInput);
  const data: string = readInput();
  nodeSerialize.unserialize(data);
  res.json({ accepted: true });
}
