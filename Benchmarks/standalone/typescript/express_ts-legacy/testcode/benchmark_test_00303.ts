// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00303 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body.field as string) || "";
  const parts: string[] = [];
  for (const token of String(userInput).split(',')) { parts.push(token); }
  const data: string = parts.join(',');
  const planQuotas = new Map([["basic", { quota: 10 }], ["team", { quota: 50 }], ["enterprise", { quota: 500 }]]);
  const { quota } = planQuotas.get(String(data))!;
  res.json({ quota }); return;
}
