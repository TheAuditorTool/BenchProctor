// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as net from "net";

export const BenchmarkTest00063 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body.field as string) || "";
  const transform = (v: string): string => v.trim();
  const data: string = transform(userInput);
  net.connect(80, new URL(String(data)).hostname);
  res.json({ accepted: true });
}
