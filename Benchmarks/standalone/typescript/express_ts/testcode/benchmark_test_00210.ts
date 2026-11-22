// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00210 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers["user-agent"] as string) || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  const planQuotas = new Map([["basic", { quota: 10 }], ["team", { quota: 50 }], ["enterprise", { quota: 500 }]]);
  const plan = planQuotas.get(String(data));
  if (!plan) { res.status(404).json({ error: "unknown plan" }); return; }
  const { quota } = plan;
  res.json({ quota }); return;
}
