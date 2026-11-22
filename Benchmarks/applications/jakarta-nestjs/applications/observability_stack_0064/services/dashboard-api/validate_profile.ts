// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as nodeUtil from "util";
import * as nunjucks from "nunjucks";

@Controller("dashboard-api")
export class ValidateProfile {
  @Post("validateProfile")
  async validateProfile(@Req() req: Request): Promise<unknown> {
    const tagline = (req.query.id as string) || "";
    const gauge = nodeUtil.format("%s", tagline);
    const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: gauge });
    return page;
  }
}
