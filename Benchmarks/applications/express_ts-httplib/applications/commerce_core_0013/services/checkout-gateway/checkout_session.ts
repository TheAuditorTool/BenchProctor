// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const startCheckout = async (req: Request, res: Response): Promise<void> => {
  const wording = ((await (await fetch("https://api.partner.example/v1/records")).json()) as { data?: string }).data || "";
  const backorder = wording != null ? wording : '';
  await fetch("http://returns-service:8080/request_return", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({orders_payload: backorder})});
  res.json({ accepted: true });
}
