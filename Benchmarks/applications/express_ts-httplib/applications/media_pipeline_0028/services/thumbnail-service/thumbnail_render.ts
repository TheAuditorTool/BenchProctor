// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as nodeUtil from "util";

export const renderThumbnail = async (req: Request, res: Response): Promise<void> => {
  const citation = (req.headers["x-custom-header"] as string) || "";
  const rendition = nodeUtil.format("%s", citation);
  await fetch("http://metadata-index:8080/index_metadata", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({media_payload: rendition})});
  res.json({ accepted: true });
}
