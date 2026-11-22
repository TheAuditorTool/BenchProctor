// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const settleCapture = async (req: Request, res: Response): Promise<void> => {
  const memo = (req.params.id as string) || "";
  let ledger: string = '';
  const onInput = (v: string): void => { ledger = v; };
  onInput(memo);
  await fetch("http://payout-service:8000/schedule_payout", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({payments_payload: ledger})});
  res.json({ accepted: true });
}
