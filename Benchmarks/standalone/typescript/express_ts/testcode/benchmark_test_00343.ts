// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as nunjucks from "nunjucks";

export const BenchmarkTest00343 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body as string) || "";
  const [data] = String(userInput).split(',');
  const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: data });
  res.send(page);
}
