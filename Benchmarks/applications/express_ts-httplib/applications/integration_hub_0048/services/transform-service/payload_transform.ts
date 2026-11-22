// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const transformPayload = async (req: Request, res: Response): Promise<void> => {
  const citation = (req.params.id as string) || "";
  const transform = (v: string): string => v.trim();
  const handshake: string = transform(citation);
  await fetch("http://partner-registry:8080/register_partner", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({integrations_payload: handshake})});
  res.json({ accepted: true });
}
