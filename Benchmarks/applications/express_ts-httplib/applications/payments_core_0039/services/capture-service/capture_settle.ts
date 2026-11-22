// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";

export const settleCapture = async (req: Request, res: Response): Promise<void> => {
  const memo = (await shared.mq.receive("app-events"));
  const transform = (v: string): string => v.trim();
  const ledger: string = transform(memo);
  await fetch("http://payout-service:8080/schedule_payout", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({payments_payload: ledger})});
  res.json({ accepted: true });
}
