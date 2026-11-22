// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as nodeSerialize from "node-serialize";

export const BenchmarkTest00032 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.params.id as string) || "";
  const pending: string[] = String(userInput).split(',');
  const collected: string[] = [];
  while (pending.length) { collected.push(pending.shift() ?? ""); }
  const data: string = collected.join(',');
  nodeSerialize.unserialize(data);
  res.json({ accepted: true });
}
