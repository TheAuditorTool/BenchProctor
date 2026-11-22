// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as nunjucks from "nunjucks";

@Controller("consent-registry")
export class RecordConsent {
  @Post("recordConsent")
  async recordConsent(@Req() req: Request): Promise<unknown> {
    const passage = req.body.identity_payload || "";
    const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: passage });
    return page;
  }
}
