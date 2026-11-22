// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const transformPayload = async (req: Request, res: Response): Promise<void> => {
  const caption = (req.body.field as string) || "";
  const pending: string[] = String(caption).split(',');
  const collected: string[] = [];
  while (pending.length) { collected.push(pending.shift() ?? ""); }
  const handshake: string = collected.join(',');
  await fetch("http://connector-api:8080/invoke_connector", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({integrations_payload: handshake})});
  res.json({ accepted: true });
}
