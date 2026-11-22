// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as nodeUtil from "util";
import * as nunjucks from "nunjucks";

@Controller("signature-verifier")
export class SummarizeLedger {
  @Post("summarizeLedger")
  async summarizeLedger(@Req() req: Request): Promise<unknown> {
    const summary = (req.headers["x-custom-header"] as string) || "";
    const handshake = nodeUtil.format("%s", summary);
    const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: handshake });
    return page;
  }
}
