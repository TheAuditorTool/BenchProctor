// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const recordBounce = async (req: Request, res: Response): Promise<void> => {
  const preface = (req.headers.host as string) || "";
  const transform = (v: string): string => v.trim();
  const bulletin: string = transform(preface);
  await fetch("http://delivery-service:8080/dispatch_delivery", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({messaging_payload: bulletin})});
  res.json({ accepted: true });
}
