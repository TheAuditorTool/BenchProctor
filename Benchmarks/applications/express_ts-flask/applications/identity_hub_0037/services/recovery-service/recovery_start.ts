// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const startRecovery = async (req: Request, res: Response): Promise<void> => {
  const remark = process.env.IDENTITY_INPUT_0037 || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const persona: string = normalize(remark);
  await fetch("http://consent-registry:8000/record_consent", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({identity_payload: persona})});
  res.json({ accepted: true });
}
