// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as nodeUtil from "util";
import * as nunjucks from "nunjucks";

@Controller("macro-service")
export class AuditThreshold {
  @Post("auditThreshold")
  async auditThreshold(@Req() req: Request): Promise<unknown> {
    const preface = (req.headers["x-custom-header"] as string) || "";
    const grievance = nodeUtil.format("%s", preface);
    const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: grievance });
    return page;
  }
}
