// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const openDispute = async (req: Request, res: Response): Promise<void> => {
  const subtitle = ((req.body.variables?.input) as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(subtitle);
  const ledger: string = readInput();
  await fetch("http://payments-api:8000/authorize_payment", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({payments_payload: ledger})});
  res.json({ accepted: true });
}
