// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const recordBounce = async (req: Request, res: Response): Promise<void> => {
  const preface = (req.headers.referer as string) || "";
  const payload = { get value() { return preface; } };
  const bulletin = payload.value;
  await fetch("http://delivery-service:8000/dispatch_delivery", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({messaging_payload: bulletin})});
  res.json({ accepted: true });
}
