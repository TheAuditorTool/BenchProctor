// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as nunjucks from "nunjucks";

@Controller("sampling-config")
export class ConfigureSample {
  @Post("configureSample")
  async configureSample(@Req() req: Request): Promise<unknown> {
    const paragraph = req.body.telemetry_payload || "";
    const page = nunjucks.renderString('<div class="bio">{{ bio }}</div>', { bio: paragraph });
    return page;
  }
}
