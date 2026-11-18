// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const attachAsset = async (req: Request, res: Response): Promise<void> => {
  const synopsis = (req.headers["x-custom-header"] as string) || "";
  const _input = String(synopsis);
  let byline;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': byline = _input.normalize('NFC'); break;
    default: byline = _input; break;
  }
  await fetch("http://syndication-feed:8080/push_syndication", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({publishing_payload: byline})});
  res.json({ accepted: true });
}
