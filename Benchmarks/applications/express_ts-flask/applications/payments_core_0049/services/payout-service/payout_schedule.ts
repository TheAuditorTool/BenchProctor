// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const schedulePayout = async (req: Request, res: Response): Promise<void> => {
  const headline = (req.headers.referer as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(headline);
  const disbursement: string = readInput();
  await fetch("http://reconcile-service:8000/run_reconciliation", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({payments_payload: disbursement})});
  res.json({ accepted: true });
}
