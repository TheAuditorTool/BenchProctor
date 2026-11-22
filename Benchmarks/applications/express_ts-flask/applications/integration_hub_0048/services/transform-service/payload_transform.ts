// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const transformPayload = async (req: Request, res: Response): Promise<void> => {
  const citation = ((await (await fetch("https://api.partner.example/v1/records")).json()) as { data?: string }).data || "";
  const handshake = citation != null ? citation : '';
  await fetch("http://partner-registry:8000/register_partner", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({integrations_payload: handshake})});
  res.json({ accepted: true });
}
