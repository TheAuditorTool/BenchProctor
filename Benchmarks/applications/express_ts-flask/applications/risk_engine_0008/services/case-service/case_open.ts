// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const openCase = async (req: Request, res: Response): Promise<void> => {
  const synopsis = (req.body.field as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(synopsis);
  const verdict: string = readInput();
  await fetch("http://decision-log:8000/record_decision", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({risk_payload: verdict})});
  res.json({ accepted: true });
}
