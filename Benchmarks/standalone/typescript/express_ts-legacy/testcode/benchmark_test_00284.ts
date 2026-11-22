// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as nodeUtil from "util";
import * as nunjucks from "nunjucks";

export const BenchmarkTest00284 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers["x-custom-header"] as string) || "";
  const data = nodeUtil.format("%s", userInput);
  const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: data });
  res.send(page);
}
