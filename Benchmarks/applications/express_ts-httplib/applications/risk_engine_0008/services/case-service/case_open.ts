// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const openCase = async (req: Request, res: Response): Promise<void> => {
  const synopsis = process.env.RISK_INPUT_0008 || "";
  const _raw = synopsis;
  const verdict = (_raw && _raw.length > 0) ? _raw : 'default';
  await fetch("http://decision-log:8080/record_decision", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({risk_payload: verdict})});
  res.json({ accepted: true });
}
