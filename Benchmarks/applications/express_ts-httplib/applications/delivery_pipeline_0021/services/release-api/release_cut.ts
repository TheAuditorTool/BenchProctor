// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const cutRelease = async (req: Request, res: Response): Promise<void> => {
  const summary = process.env.DELIVERY_INPUT_0021 || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const phrase: string = normalize(summary);
  await fetch("http://rollback-service:8080/trigger_rollback", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({delivery_payload: phrase})});
  res.json({ accepted: true });
}
