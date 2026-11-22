// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as nunjucks from "nunjucks";

export const archiveWebhook = async (req: Request, res: Response): Promise<void> => {
  const heading = (req.headers["user-agent"] as string) || "";
  const handshake = heading != null ? heading : '';
  const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: handshake });
  res.send(page);
}
